# Generated by Django 3.0.6 on 2020-07-10 08:21

import admin_manage_grape.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_manage_grape', '0005_awgrape_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='awgrape',
            name='Grape_banner_Image',
            field=models.ImageField(blank=True, null=True, upload_to=admin_manage_grape.models.user_directory_path_banner),
        ),
    ]
