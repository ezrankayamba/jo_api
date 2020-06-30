from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models
import datetime
import requests
import json
import configparser

# Create your views here.


def get_conf():
    config = configparser.ConfigParser()
    config.sections()
    read = config.read('oauth.ini')
    print(read)
    DEFAULT = config['DEFAULT']
    return DEFAULT


oauth_conf = get_conf()


class JoFetchToken(APIView):
    permission_classes = []

    def post(self, request):
        username = request.data['username'] if 'username' in request.data else None
        password = request.data['password'] if 'password' in request.data else None

        if username and password:
            client_id = oauth_conf['client_id']
            client_secret = oauth_conf['client_secret']
            data = f'username={username}&password={password}&grant_type=password&client_id={client_id}&client_secret={client_secret}'
            headers = {'Content-Type': 'application/x-www-form-urlencoded'}
            res = requests.post("http://localhost:8000/api/oauth2/token/", data=data, headers=headers)
            content = json.loads(res.content)
            if 'access_token' in content:
                return Response({"statusCode": 200, "statusMessage": "Successfully fetched token", "result": json.loads(res.content)})
            else:
                return Response({"statusCode": 401, "statusMessage": "Authentication failed, check details and resubmit"})
        else:
            return Response({"statusCode": 401, "statusMessage": "Empty username or password"})


class JoAPI(APIView):
    permission_classes = []

    def str_date_to_fmt(self, dt_obj):
        # dt_obj = datetime.datetime.strptime(dt_str, '%Y-%m-%dT%H:%M:%SZ')
        new_dt_str = dt_obj.strftime('%Y-%m-%d')
        return new_dt_str

    def get_data(self, ip_address=None, start_date=None, start_jo=None):
        sql = 'SELECT u.fullname, u.joDivision, a.joStatus, a.joAuthoriserEmail, a.joApprovedDate, e.ne_commonname, e.ne_hostname, e.ne_ip, j.* FROM `jobs` j left join users u on j.requestor = u.username left join joauthoriser a on j.jo_id = a.jo_id left join jo_affected_ne f on j.jo_id=f.af_jo_id left join jo_network_elements e on j.jo_id = f.af_jo_id AND f.af_ne_id = e.ne_id where 1=1 '
        params = []
        if ip_address:
            sql = f'{sql} and ne_ip = %s '
            params.append(ip_address)

        if start_date:
            sql = f'{sql} and thedate >= %s '
            params.append(f'20{start_date}')

        if start_jo:
            sql = f'{sql} and j.jo_id >= %s '
            params.append(start_jo)

        rs = models.Jobs.objects.raw(sql, params)
        data = []
        for row in rs:
            approval = []
            for appr in models.Joauthoriser.objects.filter(jo_id=row.jo_id):
                approval.append({
                    'Approval Status': appr.jostatus,
                    'Approver': appr.joauthoriseremail,
                    'Approval Date': self.str_date_to_fmt(appr.joapproveddate),
                })
            sys_changed = []
            sys_sql = f'SELECT f.af_ne_id, e.* from jo_affected_ne f left join jo_network_elements e on f.af_ne_id = e.ne_id where f.af_jo_id = %s'
            for ne in models.JoAffectedNe.objects.raw(sys_sql, [row.jo_id]):
                sys_changed.append({
                    'System Name': ne.ne_commonname,
                    'Ip Address': ne.ne_ip,
                })
            data.append({
                'Identifier': row.jo_id,
                'Requestor': row.fullname,
                'Requestor Email': row.requestor,
                'Requestor Department': row.joDivision,
                'Request Date': self.str_date_to_fmt(row.thedate),
                'CAB Ref Number': row.support_ref_number,
                'JO Number': row.jo_number,
                'JO Type': row.job_status,
                'JOB Title': row.subject,
                'Approval': approval,
                'Systems to be changed': sys_changed,
                'Mitigation Plan': row.mitigation_in_place,
            })
        return data

    def post(self, request):
        params = request.data['Params'] if 'Params' in request.data else None
        if params:
            ip_address = params['IP Address'] if 'IP Address' in params else None
            start_date = params['Start Date'] if 'Start Date' in params else None
            start_jo = params['Start JO'] if 'Start JO' in params else None
        data = self.get_data(ip_address, start_date, start_jo)
        return Response({
            'statusCode': 200,
            'statusMessage': f'Success',
            'results': data
        })
