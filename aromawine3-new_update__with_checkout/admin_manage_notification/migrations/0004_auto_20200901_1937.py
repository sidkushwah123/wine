# Generated by Django 3.0.6 on 2020-09-01 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_manage_notification', '0003_auto_20200901_1856'),
    ]

    operations = [
        migrations.AddField(
            model_name='awnotification',
            name='Read_Status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='awnotification',
            name='Read_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
