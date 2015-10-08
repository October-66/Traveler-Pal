# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_activity_launcheddate'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='endDateTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 8, 3, 41, 51, 916769, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='activity',
            name='startDateTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 8, 3, 41, 51, 916769, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='activityuser',
            name='joinedDate',
            field=models.DateField(default=datetime.datetime(2015, 10, 8, 3, 41, 51, 916769, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='activity',
            name='launchedDate',
            field=models.DateField(default=datetime.datetime(2015, 10, 8, 3, 41, 51, 916769, tzinfo=utc)),
        ),
    ]
