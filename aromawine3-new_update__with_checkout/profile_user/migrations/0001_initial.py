# Generated by Django 3.0.6 on 2020-07-09 08:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AwUserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=120)),
                ('Contact_no', models.IntegerField(default=0)),
                ('User', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='User_AwUserInfo', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Aw User Infg',
            },
        ),
    ]
