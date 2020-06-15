import django
from django.db import models
from django.utils import timezone


# Create your models here.


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    SNAME = models.CharField(max_length=32, null=True)
    SVALID = models.BooleanField(default=1)

    class Meta:
        app_label = "Market"


class StudentInfo(models.Model):
    SID = models.OneToOneField(Student, on_delete=models.PROTECT, null=True)
    SAVATAR = models.CharField(max_length=128, null=True)
    SSEX = models.BooleanField(null=True)
    SMAJOR = models.CharField(max_length=32, null=True)
    SADDRESS = models.CharField(max_length=32, null=True)
    SRATING = models.IntegerField(default=0, null=True)

    class Meta:
        app_label = "Market"


class Commodity(models.Model):
    id = models.AutoField(primary_key=True)
    SID = models.ForeignKey(Student, on_delete=models.PROTECT, null=True)
    CNAME = models.CharField(max_length=32, null=True)
    CQUANTITY = models.IntegerField(null=True)
    CPRICE = models.DecimalField(decimal_places=2, max_digits=6, null=True)
    CISSOLD = models.BooleanField(default=0, null=False)
    is_delete = models.BooleanField(default=0, null=False)
    CDATE = models.DateTimeField(default=django.utils.timezone.now)

    class Meta:
        app_label = "Market"


class CommodityInfo(models.Model):
    CID = models.OneToOneField(Commodity, on_delete=models.PROTECT, null=True)
    CIMAGE = models.CharField(max_length=128, null=True)
    CDESCRIPTION = models.CharField(max_length=255, null=True)
    CLIKES = models.IntegerField(null=False, default=0)
    CSTARS = models.IntegerField(null=False, default=0)
    SID = models.ForeignKey(Student, on_delete=models.PROTECT, null=True)

    class Meta:
        app_label = "Market"


class Notice(models.Model):
    id = models.AutoField(primary_key=True)
    SID = models.ForeignKey(Student, on_delete=models.PROTECT, null=True)
    NCONTENT = models.CharField(max_length=255, null=True)
    NISREAD = models.BooleanField(null=False, default=0)

    class Meta:
        app_label = "Market"


class Rating(models.Model):
    CID = models.OneToOneField(Commodity, on_delete=models.PROTECT, null=True)
    SID = models.ForeignKey(Student, on_delete=models.PROTECT, null=True)
    RATING = models.IntegerField(null=True)

    class Meta:
        app_label = "Market"


class StuStars(models.Model):
    SID = models.ForeignKey(Student, on_delete=models.PROTECT, null=True)
    CID = models.ForeignKey(Commodity, on_delete=models.PROTECT, null=True)

    class Meta:
        app_label = "Market"


class StuLikes(models.Model):
    SID = models.ForeignKey(Student, on_delete=models.PROTECT, null=True)
    CID = models.ForeignKey(Commodity, on_delete=models.PROTECT, null=True)

    class Meta:
        app_label = "Market"
