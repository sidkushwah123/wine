# Generated by Django 3.0.6 on 2020-07-09 08:29

import admin_manage_region.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('admin_manage_country', '0001_initial'),
        ('admin_manage_producer', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AwRegion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Region_Name', models.CharField(max_length=120, unique=True)),
                ('Slug', models.CharField(blank=True, max_length=120, null=True, unique=True)),
                ('Region_Image', models.ImageField(upload_to=admin_manage_region.models.user_directory_path)),
                ('Description', models.TextField(blank=True, null=True)),
                ('Status', models.BooleanField(default=True)),
                ('Created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('Updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('Country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='AwRegion_Country', to='admin_manage_country.AwCountry')),
                ('Created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='AwRegion_Created_by', to=settings.AUTH_USER_MODEL)),
                ('Set_To', models.ManyToManyField(blank=True, related_name='AwRegion_set_to', to='admin_manage_producer.AwSetTo')),
                ('Updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='AwRegion_Updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'AW Region',
            },
        ),
    ]
