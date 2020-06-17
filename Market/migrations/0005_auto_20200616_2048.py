# Generated by Django 3.0.7 on 2020-06-16 12:48

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Market', '0004_auto_20200615_1720'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commodity',
            old_name='SID',
            new_name='student',
        ),
        migrations.RenameField(
            model_name='commodityinfo',
            old_name='CID',
            new_name='commodity',
        ),
        migrations.RenameField(
            model_name='notice',
            old_name='SID',
            new_name='student',
        ),
        migrations.RenameField(
            model_name='rating',
            old_name='CID',
            new_name='commodity',
        ),
        migrations.RenameField(
            model_name='rating',
            old_name='SID',
            new_name='student',
        ),
        migrations.RenameField(
            model_name='studentinfo',
            old_name='SID',
            new_name='student',
        ),
        migrations.RenameField(
            model_name='stulikes',
            old_name='CID',
            new_name='commodity',
        ),
        migrations.RenameField(
            model_name='stulikes',
            old_name='SID',
            new_name='student',
        ),
        migrations.RenameField(
            model_name='stustars',
            old_name='CID',
            new_name='commodity',
        ),
        migrations.RenameField(
            model_name='stustars',
            old_name='SID',
            new_name='student',
        ),
        migrations.RemoveField(
            model_name='commodity',
            name='CQUANTITY',
        ),
        migrations.RemoveField(
            model_name='commodityinfo',
            name='CIMAGE',
        ),
        migrations.RemoveField(
            model_name='commodityinfo',
            name='SID',
        ),
        migrations.AddField(
            model_name='commodity',
            name='CIMAGE',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='commodityinfo',
            name='CQUANTITY',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='notice',
            name='NDATE',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='SNICKNAME',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='RATING',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('HDATE', models.DateTimeField(default=django.utils.timezone.now)),
                ('buyer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Market.Student')),
                ('commodity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Market.Commodity')),
            ],
        ),
    ]
