# Generated by Django 3.0.6 on 2020-10-16 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0019_aworders_order_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='aworders',
            name='Order_Gst_Amount',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='aworders',
            name='Order_Product_Amount',
            field=models.FloatField(default=0),
        ),
    ]
