# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20151008_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='endDateTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 24, 14, 56, 10, 655000, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='launchedDateTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 24, 14, 56, 10, 655000, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='startDateTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 24, 14, 56, 10, 655000, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='postable',
            name='postDateTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 24, 14, 56, 10, 655000, tzinfo=utc), null=True),
        ),
    ]
