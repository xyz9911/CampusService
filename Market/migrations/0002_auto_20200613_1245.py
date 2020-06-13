# Generated by Django 3.0.7 on 2020-06-13 04:45

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Market', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commodity',
            old_name='UID',
            new_name='SID',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='UNAME',
            new_name='SNAME',
        ),
        migrations.RemoveField(
            model_name='commodity',
            name='CID',
        ),
        migrations.RemoveField(
            model_name='notice',
            name='NID',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='RID',
        ),
        migrations.RemoveField(
            model_name='student',
            name='UID',
        ),
        migrations.RemoveField(
            model_name='student',
            name='UVALID',
        ),
        migrations.RemoveField(
            model_name='studentinfo',
            name='UADDRESS',
        ),
        migrations.RemoveField(
            model_name='studentinfo',
            name='UID',
        ),
        migrations.RemoveField(
            model_name='studentinfo',
            name='UMAJOR',
        ),
        migrations.RemoveField(
            model_name='studentinfo',
            name='URATING',
        ),
        migrations.RemoveField(
            model_name='studentinfo',
            name='USEX',
        ),
        migrations.AddField(
            model_name='commodityinfo',
            name='CIMAGE',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='SVALID',
            field=models.BooleanField(default=1),
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='SADDRESS',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='SAVATAR',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='SID',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='Market.Student'),
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='SMAJOR',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='SRATING',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='SSEX',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='commodity',
            name='CDATE',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='commodity',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='commodityinfo',
            name='CDESCRIPTION',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='commodityinfo',
            name='CID',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='Market.Commodity'),
        ),
        migrations.AlterField(
            model_name='commodityinfo',
            name='CLIKES',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='commodityinfo',
            name='CSTARS',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='notice',
            name='NCONTENT',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='notice',
            name='NISREAD',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='notice',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='rating',
            name='CID',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='Market.Commodity'),
        ),
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
