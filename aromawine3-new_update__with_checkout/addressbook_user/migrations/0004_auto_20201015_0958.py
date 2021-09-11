# Generated by Django 3.0.6 on 2020-10-15 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_manage_setting', '0007_auto_20201015_0716'),
        ('addressbook_user', '0003_auto_20200906_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='awaddressbook',
            name='Country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='country_Address', to='admin_manage_setting.AwManageShipping'),
        ),
    ]