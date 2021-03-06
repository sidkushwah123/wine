# Generated by Django 3.0.8 on 2020-07-15 14:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('admin_manage_perferences', '0004_auto_20200715_0144'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Service_Interests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Service_interests_by_user', models.CharField(max_length=120)),
                ('Date', models.DateTimeField(default=django.utils.timezone.now)),
                ('Interested_User', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='service_interests_user', to=settings.AUTH_USER_MODEL)),
                ('Service_interest', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='service_interests_name', to='admin_manage_perferences.Service_Interests')),
            ],
            options={
                'verbose_name_plural': 'Aw User Service Interests',
            },
        ),
    ]
