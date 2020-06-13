# Generated by Django 3.0.7 on 2020-06-12 13:25

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CID', models.IntegerField(null=True)),
                ('CNAME', models.CharField(max_length=32, null=True)),
                ('CPRICE', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('CDATE', models.DateTimeField(default=datetime.datetime(2020, 6, 12, 13, 25, 25, 676795, tzinfo=utc), null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UID', models.IntegerField(null=True)),
                ('UNAME', models.CharField(max_length=32, null=True)),
                ('UVALID', models.BooleanField(default=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('USEX', models.BooleanField()),
                ('UMAJOR', models.CharField(max_length=32)),
                ('UADDRESS', models.CharField(max_length=32)),
                ('URATING', models.IntegerField(default=0)),
                ('UID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Market.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RID', models.IntegerField(null=True)),
                ('RATING', models.IntegerField(null=True)),
                ('CID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Market.Commodity')),
                ('SID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Market.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NID', models.IntegerField(null=True)),
                ('NCONTENT', models.CharField(max_length=1000, null=True)),
                ('NISREAD', models.BooleanField(default=0, null=True)),
                ('SID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Market.Student')),
            ],
        ),
        migrations.CreateModel(
            name='CommodityInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CDESCRIPTION', models.CharField(max_length=1000, null=True)),
                ('CQUANTITY', models.IntegerField(null=True)),
                ('CLIKES', models.IntegerField(default=0, null=True)),
                ('CSTARS', models.IntegerField(default=0, null=True)),
                ('CID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Market.Commodity')),
            ],
        ),
        migrations.AddField(
            model_name='commodity',
            name='UID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Market.Student'),
        ),
    ]