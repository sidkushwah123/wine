# Generated by Django 3.0.6 on 2020-07-18 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_manage_producer', '0002_awproducers_producer_banner_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='awproducers',
            name='Short_Description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
