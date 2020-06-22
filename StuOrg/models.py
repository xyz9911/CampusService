import django
from django.db import models
from django.utils import timezone


# Create your models here.

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    SNAME = models.CharField(max_length=32, null=True)

    class Meta:
        app_label = "StuOrg"


class StudentInfo(models.Model):
    student = models.OneToOneField(Student, on_delete=models.PROTECT, null=True)
    SSEX = models.BooleanField(null=True)
    SMAJOR = models.CharField(max_length=32, null=True)
    SINTRO = models.TextField(null=True)

    class Meta:
        app_label = "StuOrg"


class Organization(models.Model):
    id = models.AutoField(primary_key=True)
    ONAME = models.CharField(max_length=32, null=True)
    OIMAGE=models.CharField(max_length=255, null=True)
    ODESCRIPTION = models.CharField(max_length=255, null=True)

    class Meta:
        app_label = "StuOrg"


class OrgCharge(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT, null=True)
    student = models.ForeignKey(Student, on_delete=models.PROTECT, null=True)
    SDUTY = models.CharField(max_length=32, null=True)
    OTIME = models.DateField(default=django.utils.timezone.now, null=False)

    class Meta:
        app_label = "StuOrg"


class OrgStu(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT, null=True)
    student = models.ForeignKey(Student, on_delete=models.PROTECT, null=True)
    OTIME = models.DateField(default=django.utils.timezone.now, null=False)

    class Meta:
        app_label = "StuOrg"


class Notice(models.Model):
    id = models.AutoField(primary_key=True)
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT, null=True)
    NCONTENT = models.TextField(max_length=1024, null=True)
    NTIME = models.DateField(default=django.utils.timezone.now, null=False)

    class Meta:
        app_label = "StuOrg"


class NoticeStu(models.Model):
    notice = models.ForeignKey(Notice, on_delete=models.PROTECT, null=True)
    student = models.ForeignKey(Student, on_delete=models.PROTECT, null=True)
    NISREAD = models.BooleanField(default=False, null=False)

    class Meta:
        app_label = "StuOrg"
