# Generated by Django 3.0.6 on 2020-07-14 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_manage_products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='awproducts',
            name='Product_image',
            field=models.TextField(blank=True, null=True),
        ),
    ]
