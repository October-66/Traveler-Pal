# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='endDateTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 8, 6, 25, 11, 253684, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='launchedDateTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 8, 6, 25, 11, 253684, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='startDateTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 8, 6, 25, 11, 253684, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='postable',
            name='postDateTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 8, 6, 25, 11, 253684, tzinfo=utc), null=True),
        ),
    ]
