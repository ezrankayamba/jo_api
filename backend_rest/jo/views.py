from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from . import models
import datetime
import requests
import json
import configparser
from datetime import datetime, timedelta

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
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data['username'] if 'username' in request.data else None
        password = request.data['password'] if 'password' in request.data else None

        if username and password:
            client_id = oauth_conf['client_id']
            client_secret = oauth_conf['client_secret']
            oauth_url = oauth_conf['oauth_url']
            data = f'username={username}&password={password}&grant_type=password&client_id={client_id}&client_secret={client_secret}'
            headers = {'Content-Type': 'application/x-www-form-urlencoded'}
            res = requests.post(oauth_url, data=data, headers=headers)
            content = json.loads(res.content)
            if 'access_token' in content:
                return Response({"statusCode": 200, "statusMessage": "Successfully fetched token", "result": json.loads(res.content)})
            else:
                return Response({"statusCode": 401, "statusMessage": "Authentication failed, check details and resubmit"})
        else:
            return Response({"statusCode": 401, "statusMessage": "Empty username or password"})


class JoAPI(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def str_date_to_fmt(self, dt_obj):
        new_dt_str = dt_obj.strftime('%Y-%m-%d')
        return new_dt_str

    def get_data(self, ip_address=None, start_date=None, range_hours=None):
        print(f'IP: {ip_address}, Date: {start_date}, RangeHours: {range_hours}')
        sql = "SELECT u.fullname, u.joDivision, j.* FROM `jobs` j left join users u on j.requestor = u.username where j.jobstatus in ('BROADCASTED', 'SUCCESSFUL', 'UNSUCCESSFUL', 'ONGOING', 'PAUSED', 'POSTPONED', 'CANCELLED')"
        params = []

        if range_hours:
            d = datetime.today() - timedelta(hours=range_hours)
            new_start_date = d.strftime('%Y-%m-%d %H:%M:%S')
        else:
            new_start_date = start_date

        if new_start_date:
            sql = f"{sql} and ((j.jobstatus = 'PAUSED') or (j.jobstatus = 'BROADCASTED' and broadcastDate >= %s) or (j.jobstatus in ('SUCCESSFUL', 'UNSUCCESSFUL', 'ONGOING', 'POSTPONED', 'CANCELLED') and executionComment >= %s)) "
            params.extend([f'20{new_start_date}'] * 2)

        rs = models.Jobs.objects.raw(sql, params)
        data = []
        for row in rs:
            approval = []
            disapproved = False
            disapproved_date = None
            for appr in models.Joauthoriser.objects.filter(jo_id=row.jo_id).order_by('joapproveddate'):
                approval_date = self.str_date_to_fmt(appr.joapproveddate)
                approval.append({
                    'ApprovalStatus': appr.jostatus,
                    'Approver': appr.joauthoriseremail,
                    'ApprovalDate': approval_date,
                })
                if appr.jostatus == 'DISAPPROVED':
                    disapproved = True
                    disapproved_date = approval_date

            if row.jobstatus == 'PAUSED':
                if not disapproved:
                    continue
                if new_start_date and new_start_date > approval_date:
                    continue

            sys_changed = []
            sys_sql = f'SELECT f.af_ne_id, e.* from jo_affected_ne f left join jo_network_elements e on f.af_ne_id = e.ne_id where f.af_jo_id = %s'
            ip_found = False
            for ne in models.JoAffectedNe.objects.raw(sys_sql, [row.jo_id]):
                sys_changed.append({
                    'SystemName': ne.ne_commonname,
                    'IpAddress': ne.ne_ip,
                })
                if ne.ne_ip == ip_address:
                    ip_found = True
            if ip_address and not ip_found:
                continue

            data.append({
                'Identifier': row.jo_id,
                'Requestor': row.fullname,
                'RequestorEmail': row.requestor,
                'RequestorDepartment': row.joDivision,
                'RequestDate': self.str_date_to_fmt(row.thedate),
                'CABRefNumber': row.support_ref_number,
                'JONumber': row.jo_number,
                'JOType': row.job_status,
                'JOStatus': row.jobstatus,
                'JOBTitle': row.subject,
                'Approval': approval,
                'JOCategory': row.change_type,
                'Purpose': row.purpose,
                'SystemsImpacted': row.affected_network_element,
                'SystemsToBeChanged': sys_changed,
                'MitigationPlan': row.mitigation_in_place,
                'StartTime': row.start_time.strftime('%Y-%m-%d %H:%m'),
                'EndTime': row.end_time.strftime('%Y-%m-%d %H:%m'),
            })
        return data

    def post(self, request):
        print("API User: ", request.user, ", Request: ", request.data)
        params = request.data['Params'] if 'Params' in request.data else None
        if params:
            ip_address = params['IPAddress'] if 'IPAddress' in params else None
            start_date = params['StartDate'] if 'StartDate' in params else None
            range_hours = params['LastNHours'] if 'LastNHours' in params else None
        data = self.get_data(ip_address, start_date, range_hours)
        return Response({
            'statusCode': 200,
            'statusMessage': f'Success',
            'results': data
        })
