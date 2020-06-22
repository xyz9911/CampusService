from django.db import models


# Create your models here.

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    SNAME = models.CharField(max_length=32, null=True)
    SPASSWORD = models.CharField(max_length=32, null=True)
    SISVALID = models.BooleanField(default=1)


class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    APASSWORD = models.CharField(max_length=32, null=True)
