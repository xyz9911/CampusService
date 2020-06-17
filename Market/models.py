import django
from django.db import models
from django.utils import timezone


# Create your models here.


class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    SNAME = models.CharField(max_length=32, null=True)
    SVALID = models.BooleanField(default=1)

    class Meta:
        app_label = "Market"


class StudentInfo(models.Model):
    # def __init__(self,stu,nickname,avatar,sex,major,address,rating):
    #     self.student=stu
    #     self.SNICKNAME=nickname
    #     self.SAVATAR=avatar
    #     self.SSEX=sex
    #     self.SMAJOR=major
    #     self.SADDRESS=address
    #     self.SRATING=rating

    student = models.OneToOneField(Student, on_delete=models.PROTECT, null=True)
    SNICKNAME = models.CharField(max_length=128, null=True)
    SAVATAR = models.CharField(max_length=128, null=True)
    SSEX = models.BooleanField(null=True)
    SMAJOR = models.CharField(max_length=32, null=True)
    SADDRESS = models.CharField(max_length=32, null=True)
    SRATING = models.IntegerField(default=0, null=True)
    SQQ=models.CharField(max_length=32, null=True)
    STEL=models.CharField(max_length=32, null=True)

    def __unicode__(self):
        return self.SNICKNAME

    class Meta:
        app_label = "Market"


class Commodity(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.PROTECT, null=True)
    CNAME = models.CharField(max_length=32, null=True)
    CIMAGE = models.CharField(max_length=128, null=True)
    CPRICE = models.DecimalField(decimal_places=2, max_digits=6, null=True)
    CISSOLD = models.BooleanField(default=0, null=False)
    is_delete = models.BooleanField(default=0, null=False)
    CDATE = models.DateTimeField(default=django.utils.timezone.now)

    class Meta:
        app_label = "Market"


class CommodityInfo(models.Model):
    commodity = models.OneToOneField(Commodity, on_delete=models.PROTECT, null=True)
    CQUANTITY = models.IntegerField(null=True)
    CDESCRIPTION = models.CharField(max_length=255, null=True)
    CLIKES = models.IntegerField(null=False, default=0)
    CSTARS = models.IntegerField(null=False, default=0)

    class Meta:
        app_label = "Market"


class Notice(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.PROTECT, null=True)
    NCONTENT = models.CharField(max_length=255, null=True)
    NISREAD = models.BooleanField(null=False, default=0)
    NDATE = models.DateTimeField(null=False, default=django.utils.timezone.now)

    class Meta:
        app_label = "Market"


class Rating(models.Model):
    id = models.AutoField(primary_key=True)
    commodity = models.OneToOneField(Commodity, on_delete=models.PROTECT, null=True)
    student = models.ForeignKey(Student, on_delete=models.PROTECT, null=True)
    RATING = models.IntegerField(null=True)

    class Meta:
        app_label = "Market"


class History(models.Model):
    id = models.AutoField(primary_key=True)
    buyer = models.ForeignKey(Student, on_delete=models.PROTECT, null=True)
    commodity = models.ForeignKey(Commodity, on_delete=models.PROTECT, null=True)
    HDATE = models.DateTimeField(null=False, default=django.utils.timezone.now)


class StuStars(models.Model):
    student = models.ForeignKey(Student, on_delete=models.PROTECT, null=True)
    commodity = models.ForeignKey(Commodity, on_delete=models.PROTECT, null=True)

    class Meta:
        app_label = "Market"


class StuLikes(models.Model):
    student = models.ForeignKey(Student, on_delete=models.PROTECT, null=True)
    commodity = models.ForeignKey(Commodity, on_delete=models.PROTECT, null=True)

    class Meta:
        app_label = "Market"
