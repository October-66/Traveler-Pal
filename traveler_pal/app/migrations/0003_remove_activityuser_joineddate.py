# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_activity_launcheddate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activityuser',
            name='joinedDate',
        ),
    ]
