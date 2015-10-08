# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20151008_1141'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='launchedDate',
            field=models.DateField(default=datetime.datetime(2015, 10, 8, 3, 41, 37, 781752, tzinfo=utc)),
        ),
    ]
