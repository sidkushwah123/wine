# Generated by Django 3.0.6 on 2020-08-22 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_awaddtocard_cost'),
    ]

    operations = [
        migrations.RenameField(
            model_name='awaddtocard',
            old_name='Cost',
            new_name='Old_Cost',
        ),
    ]
