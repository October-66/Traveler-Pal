# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20151008_1141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='info',
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='interest',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='endDateTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 8, 3, 48, 13, 988385, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='launchedDate',
            field=models.DateField(default=datetime.datetime(2015, 10, 8, 3, 48, 13, 988385, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='startDateTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 8, 3, 48, 13, 988385, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='activityuser',
            name='joinedDate',
            field=models.DateField(default=datetime.datetime(2015, 10, 8, 3, 48, 13, 988385, tzinfo=utc), null=True),
        ),
        migrations.DeleteModel(
            name='UserInfo',
        ),
    ]
