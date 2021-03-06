# Generated by Django 3.0.7 on 2020-06-13 05:29

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('NCONTENT', models.TextField(max_length=1024, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ONAME', models.CharField(max_length=32, null=True)),
                ('ODESCRIPTION', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('SNAME', models.CharField(max_length=32, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SSEX', models.BooleanField(null=True)),
                ('SMAJOR', models.CharField(max_length=32, null=True)),
                ('SADDRESS', models.CharField(max_length=32, null=True)),
                ('SRATING', models.IntegerField(default=0, null=True)),
                ('SID', models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='StuOrg.Student')),
            ],
        ),
        migrations.CreateModel(
            name='OrgStu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OTIME', models.DateField(default=django.utils.timezone.now)),
                ('OID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='StuOrg.Organization')),
                ('SID', models.ManyToManyField(to='StuOrg.Student')),
            ],
        ),
        migrations.CreateModel(
            name='OrgCharge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SDUTY', models.CharField(max_length=32, null=True)),
                ('OTIME', models.DateField(default=django.utils.timezone.now)),
                ('OID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='StuOrg.Organization')),
                ('SID', models.ManyToManyField(to='StuOrg.Student')),
            ],
        ),
        migrations.CreateModel(
            name='NoticeStu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NISREAD', models.BooleanField(default=False)),
                ('NID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='StuOrg.Notice')),
                ('SID', models.ManyToManyField(to='StuOrg.Student')),
            ],
        ),
        migrations.AddField(
            model_name='notice',
            name='SID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='StuOrg.Student'),
        ),
    ]
