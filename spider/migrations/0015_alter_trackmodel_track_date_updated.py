# Generated by Django 4.1.1 on 2022-10-16 15:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spider', '0014_alter_trackmodel_track_date_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trackmodel',
            name='track_date_updated',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 16, 15, 11, 59, 115220, tzinfo=datetime.timezone.utc)),
        ),
    ]
