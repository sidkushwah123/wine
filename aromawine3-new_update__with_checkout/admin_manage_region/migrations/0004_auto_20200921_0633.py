# Generated by Django 3.0.6 on 2020-09-21 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_manage_region', '0003_awregion_short_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='awregion',
            old_name='Region_banner_Image',
            new_name='banner_Image',
        ),
    ]