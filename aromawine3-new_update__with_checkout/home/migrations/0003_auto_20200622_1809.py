# Generated by Django 3.0.6 on 2020-06-22 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_awcmspaage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='awcmspaage',
            name='Keyword',
        ),
        migrations.AddField(
            model_name='awcmspaage',
            name='Slug',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
