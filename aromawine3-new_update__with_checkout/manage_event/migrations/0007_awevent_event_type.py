# Generated by Django 3.0.6 on 2020-08-18 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manage_event', '0006_aweventtype_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='awevent',
            name='Event_Type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='EventType_AwEvent', to='manage_event.AwEventType'),
        ),
    ]