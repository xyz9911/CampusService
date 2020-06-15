import django
from django.db import models


# Create your models here.

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    SNAME = models.CharField(max_length=32, null=True)

    class Meta:
        app_label = "StuOrg"


class StudentInfo(models.Model):
    SID = models.OneToOneField(Student, on_delete=models.PROTECT, null=True)
    SSEX = models.BooleanField(null=True)
    SMAJOR = models.CharField(max_length=32, null=True)
    SADDRESS = models.CharField(max_length=32, null=True)
    SRATING = models.IntegerField(default=0, null=True)

    class Meta:
        app_label = "StuOrg"


class Organization(models.Model):
    id = models.AutoField(primary_key=True)
    ONAME = models.CharField(max_length=32, null=True)
    ODESCRIPTION = models.CharField(max_length=255, null=True)

    class Meta:
        app_label = "StuOrg"


class OrgCharge(models.Model):
    OID = models.ForeignKey(Organization, on_delete=models.PROTECT, null=True)
    SID = models.ForeignKey(Student, on_delete=models.PROTECT, null=True)
    SDUTY = models.CharField(max_length=32, null=True)
    OTIME = models.DateField(default=django.utils.timezone.now, null=False)

    class Meta:
        app_label = "StuOrg"


class OrgStu(models.Model):
    OID = models.ForeignKey(Organization, on_delete=models.PROTECT, null=True)
    SID = models.ForeignKey(Student, on_delete=models.PROTECT, null=True)
    OTIME = models.DateField(default=django.utils.timezone.now, null=False)

    class Meta:
        app_label = "StuOrg"


class Notice(models.Model):
    id = models.AutoField(primary_key=True)
    SID = models.ForeignKey(Student, on_delete=models.PROTECT, null=True)
    NCONTENT = models.TextField(max_length=1024, null=True)

    class Meta:
        app_label = "StuOrg"


class NoticeStu(models.Model):
    NID = models.ForeignKey(Notice, on_delete=models.PROTECT, null=True)
    SID = models.ForeignKey(Student, on_delete=models.PROTECT, null=True)
    NISREAD = models.BooleanField(default=False, null=False)

    class Meta:
        app_label = "StuOrg"
