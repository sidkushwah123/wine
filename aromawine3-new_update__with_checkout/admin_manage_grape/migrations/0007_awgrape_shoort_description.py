# Generated by Django 3.0.6 on 2020-07-18 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_manage_grape', '0006_awgrape_grape_banner_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='awgrape',
            name='Shoort_Description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
