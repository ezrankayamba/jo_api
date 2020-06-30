# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Joauthoriser(models.Model):
    jo_id = models.CharField(primary_key=True, max_length=30)
    joauthoriseremail = models.CharField(db_column='joAuthoriserEmail', max_length=45)  # Field name made lowercase.
    jocomment = models.TextField(db_column='joComment', blank=True, null=True)  # Field name made lowercase.
    # Field name made lowercase.
    jostatus = models.CharField(db_column='joStatus', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    joapproveddate = models.DateTimeField(db_column='joApprovedDate', blank=True, null=True)
    approvaltime = models.FloatField(db_column='ApprovalTime', blank=True, null=True)  # Field name made lowercase.
    sent_date = models.DateTimeField(blank=True, null=True)
    user_title = models.CharField(max_length=255)
    insert_date = models.DateTimeField(blank=True, null=True)
    proc_st = models.CharField(max_length=150, blank=True, null=True)
    email_notification_sent = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'joauthoriser'
        unique_together = (('jo_id', 'joauthoriseremail', 'user_title'),)


class Jobs(models.Model):
    jo_id = models.CharField(primary_key=True, max_length=30)
    requestor = models.CharField(max_length=75)
    subject = models.TextField()
    thedate = models.DateTimeField()
    job_status = models.CharField(max_length=100, blank=True, null=True)
    service_affecting = models.CharField(max_length=10)
    change_type = models.CharField(max_length=255)
    fms_ref = models.CharField(max_length=30)
    jo_number = models.CharField(max_length=30)
    support_ref_number = models.CharField(max_length=500, blank=True, null=True)
    purpose = models.TextField()
    general = models.TextField()
    affected_network_element = models.TextField()
    preparatory_work = models.TextField()
    action = models.TextField()
    test_plan = models.TextField()
    fallback_plan = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    implementation_officer = models.TextField(blank=True, null=True)
    controlling_officer = models.CharField(max_length=750)
    support_contact = models.CharField(max_length=750)
    completion_confirmation = models.CharField(max_length=750)
    jobstatus = models.CharField(db_column='jobStatus', max_length=20)  # Field name made lowercase.
    # Field name made lowercase.
    broadcastperson = models.CharField(db_column='broadcastPerson', max_length=75, blank=True, null=True)
    broadcastdate = models.DateTimeField(db_column='broadcastDate', blank=True, null=True)  # Field name made lowercase.
    # Field name made lowercase.
    executioncomment = models.TextField(db_column='executionComment', blank=True, null=True)
    # Field name made lowercase.
    executioncommentdate = models.DateTimeField(db_column='executionCommentDate', blank=True, null=True)
    down_time = models.TextField(blank=True, null=True)
    # Field name made lowercase.
    attachmentname = models.CharField(db_column='attachmentName', max_length=200, blank=True, null=True)
    notification = models.CharField(max_length=5)
    # Field name made lowercase.
    automaticnotice = models.IntegerField(db_column='automaticNotice', blank=True, null=True)
    start_down_time = models.TextField(blank=True, null=True)
    end_down_time = models.TextField(blank=True, null=True)
    severity = models.CharField(max_length=255, blank=True, null=True)
    priority = models.CharField(max_length=255, blank=True, null=True)
    category_group = models.CharField(max_length=255, blank=True, null=True)
    mop = models.TextField(blank=True, null=True)
    reason = models.CharField(max_length=255, blank=True, null=True)
    del_upto_date = models.DateTimeField(blank=True, null=True)
    last_remainder_notification_date = models.DateTimeField(blank=True, null=True)
    risk_type = models.CharField(max_length=150, blank=True, null=True)
    permit_reference = models.CharField(max_length=150, blank=True, null=True)
    down_time_list = models.TextField(blank=True, null=True)
    route_state = models.IntegerField(blank=True, null=True)
    proc_key = models.CharField(max_length=255, blank=True, null=True)
    change_affect_network_or_it = models.CharField(max_length=10, blank=True, null=True)
    change_affect_trp = models.CharField(max_length=50, blank=True, null=True)
    systems_to_be_changed = models.TextField(blank=True, null=True)
    cost = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    expected_results = models.TextField(blank=True, null=True)
    impact_incase = models.TextField(blank=True, null=True)
    desc_if_affect_trp = models.TextField(blank=True, null=True)
    affected_customers = models.TextField(blank=True, null=True)
    mps_type = models.CharField(max_length=255, blank=True, null=True)
    adhoc_reference = models.CharField(max_length=255, blank=True, null=True)
    change_affect_network = models.CharField(max_length=10, blank=True, null=True)
    have_adhoc_ref = models.CharField(max_length=10, blank=True, null=True)
    cost_currency = models.CharField(max_length=10, blank=True, null=True)
    cab_meeting_day = models.DateField(blank=True, null=True)
    ongoing_changed = models.IntegerField()
    cab_reminder_sent = models.IntegerField()
    ongoing_down_time = models.TextField(blank=True, null=True)
    reschedule_starttime = models.DateTimeField(blank=True, null=True)
    reschedule_endtime = models.DateTimeField(blank=True, null=True)
    security_baseline_met = models.CharField(max_length=10, blank=True, null=True)
    joversion = models.CharField(max_length=10)
    impact_type = models.CharField(max_length=255, blank=True, null=True)
    no_impact_reason = models.TextField(blank=True, null=True)
    mitigation_in_place = models.CharField(max_length=35, blank=True, null=True)
    patch_severity = models.CharField(max_length=35, blank=True, null=True)
    severity_source = models.TextField(blank=True, null=True)
    patch_source = models.TextField(blank=True, null=True)
    system_layer = models.CharField(max_length=35, blank=True, null=True)
    cmdb_assets = models.TextField(blank=True, null=True)
    accessibility = models.CharField(max_length=35, blank=True, null=True)
    test_completed = models.CharField(max_length=35, blank=True, null=True)
    is_different_plan = models.CharField(max_length=35, blank=True, null=True)
    patch_release_date = models.DateTimeField(blank=True, null=True)
    pac_meeting_day = models.DateField(blank=True, null=True)
    mitigatiton_in_place = models.CharField(max_length=35, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jobs'


class Users(models.Model):
    username = models.CharField(primary_key=True, max_length=40)
    jopassword = models.CharField(db_column='joPassword', max_length=70)  # Field name made lowercase.
    fullname = models.CharField(max_length=70)
    level = models.CharField(max_length=10, blank=True, null=True)
    telephone = models.CharField(max_length=25)
    jodivision = models.CharField(db_column='joDivision', max_length=75)  # Field name made lowercase.
    jogroup = models.CharField(db_column='joGroup', max_length=75)  # Field name made lowercase.
    jorole = models.CharField(db_column='joRole', max_length=50)  # Field name made lowercase.
    # Field name made lowercase.
    jotitle = models.CharField(db_column='joTitle', unique=True, max_length=75, blank=True, null=True)
    # Field name made lowercase.
    jodelegator = models.CharField(db_column='joDelegator', max_length=75, blank=True, null=True)
    # Field name made lowercase.
    originalrole = models.CharField(db_column='originalRole', max_length=75, blank=True, null=True)
    updatedate = models.DateTimeField(db_column='updateDate', blank=True, null=True)  # Field name made lowercase.
    del_upto_date = models.DateTimeField(blank=True, null=True)
    wrong_pass_count = models.IntegerField()
    isloggedin = models.IntegerField(db_column='isLoggedIn')  # Field name made lowercase.
    change_pass = models.IntegerField()
    change_pass_date = models.DateTimeField()
    expiredate = models.DateTimeField(db_column='expireDate', blank=True, null=True)  # Field name made lowercase.
    old_lock_role = models.CharField(max_length=50, blank=True, null=True)
    lock_datetime = models.DateTimeField(blank=True, null=True)
    wrong_pass_datetime = models.DateTimeField(blank=True, null=True)
    acctype = models.IntegerField(db_column='accType')  # Field name made lowercase.
    # Field name made lowercase.
    josection = models.CharField(db_column='joSection', max_length=255, blank=True, null=True)
    usertoken = models.CharField(max_length=255, blank=True, null=True)
    ad_username = models.CharField(unique=True, max_length=255, blank=True, null=True)
    last_logon = models.DateTimeField(blank=True, null=True)
    jo2fa_enabled = models.IntegerField()
    jo2fa_pin = models.CharField(max_length=40, blank=True, null=True)
    jo2fa_smstime = models.DateTimeField(blank=True, null=True)
    mobile_last_activity = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class JoAffectedNe(models.Model):
    af_ne = models.OneToOneField('JoNetworkElements', models.DO_NOTHING, primary_key=True)
    af_jo = models.ForeignKey(Jobs, models.DO_NOTHING)
    af_updatedate = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'jo_affected_ne'
        unique_together = (('af_ne', 'af_jo'),)


class JoNetworkElements(models.Model):
    ne_id = models.AutoField(primary_key=True)
    ne_ip = models.CharField(unique=True, max_length=20)
    ne_hostname = models.CharField(unique=True, max_length=120)
    ne_commonname = models.CharField(max_length=120)
    ne_desc = models.TextField(blank=True, null=True)
    ne_datacenter = models.CharField(max_length=75)
    ne_group = models.CharField(max_length=75)
    ne_status = models.CharField(max_length=7)

    class Meta:
        managed = False
        db_table = 'jo_network_elements'
