# Generated by Django 3.0.7 on 2020-06-17 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Market', '0005_auto_20200616_2048'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentinfo',
            name='SQQ',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='STEL',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='RATING',
            field=models.IntegerField(null=True),
        ),
    ]
