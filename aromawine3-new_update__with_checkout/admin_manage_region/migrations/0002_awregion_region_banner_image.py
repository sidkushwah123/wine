# Generated by Django 3.0.6 on 2020-07-10 12:29

import admin_manage_region.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_manage_region', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='awregion',
            name='Region_banner_Image',
            field=models.ImageField(blank=True, null=True, upload_to=admin_manage_region.models.user_directory_path_banner),
        ),
    ]
