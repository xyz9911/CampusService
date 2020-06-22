# Generated by Django 3.0.7 on 2020-06-22 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('APASSWORD', models.CharField(max_length=32, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('SNAME', models.CharField(max_length=32, null=True)),
                ('SPASSWORD', models.CharField(max_length=32, null=True)),
                ('SISVALID', models.BooleanField(default=1)),
            ],
        ),
    ]