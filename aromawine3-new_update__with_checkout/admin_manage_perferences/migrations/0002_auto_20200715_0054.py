# Generated by Django 3.0.8 on 2020-07-15 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_manage_perferences', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Wine_Interests',
        ),
        migrations.AddField(
            model_name='service_interests',
            name='Type',
            field=models.CharField(default='', max_length=120),
            preserve_default=False,
        ),
    ]
