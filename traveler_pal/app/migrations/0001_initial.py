# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=128)),
                ('launchedDateTime', models.DateTimeField(default=datetime.datetime(2015, 10, 8, 6, 24, 54, 242442, tzinfo=utc), null=True)),
                ('startDateTime', models.DateTimeField(default=datetime.datetime(2015, 10, 8, 6, 24, 54, 242442, tzinfo=utc), null=True)),
                ('endDateTime', models.DateTimeField(default=datetime.datetime(2015, 10, 8, 6, 24, 54, 242442, tzinfo=utc), null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ActivityScenery',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('activity', models.ForeignKey(null=True, to='app.Activity')),
            ],
        ),
        migrations.CreateModel(
            name='Postable',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=128)),
                ('content', models.TextField(null=True)),
                ('postDateTime', models.DateTimeField(default=datetime.datetime(2015, 10, 8, 6, 24, 54, 242442, tzinfo=utc), null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Scenery',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(null=True, max_length=128)),
                ('price', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('username', models.CharField(null=True, max_length=128)),
                ('email', models.EmailField(null=True, max_length=128)),
                ('password', models.CharField(null=True, max_length=128)),
                ('interest', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserActivity',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('activity', models.ForeignKey(null=True, to='app.Activity')),
                ('user', models.ForeignKey(null=True, to='app.User')),
            ],
        ),
        migrations.CreateModel(
            name='UserScenery',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('scenery', models.ForeignKey(null=True, to='app.Scenery')),
                ('user', models.ForeignKey(null=True, to='app.User')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('postable_ptr', models.OneToOneField(primary_key=True, to='app.Postable', parent_link=True, serialize=False, auto_created=True)),
                ('scenery', models.ForeignKey(null=True, to='app.Scenery')),
            ],
            bases=('app.postable',),
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('postable_ptr', models.OneToOneField(primary_key=True, to='app.Postable', parent_link=True, serialize=False, auto_created=True)),
            ],
            bases=('app.postable',),
        ),
        migrations.AddField(
            model_name='user',
            name='activitys',
            field=models.ManyToManyField(through='app.UserActivity', to='app.Activity'),
        ),
        migrations.AddField(
            model_name='user',
            name='scenerys',
            field=models.ManyToManyField(through='app.UserScenery', to='app.Scenery'),
        ),
        migrations.AddField(
            model_name='postable',
            name='user',
            field=models.ForeignKey(to='app.User'),
        ),
        migrations.AddField(
            model_name='activityscenery',
            name='scenery',
            field=models.ForeignKey(null=True, to='app.Scenery'),
        ),
        migrations.AddField(
            model_name='activity',
            name='scenerys',
            field=models.ManyToManyField(through='app.ActivityScenery', to='app.Scenery'),
        ),
        migrations.AddField(
            model_name='journal',
            name='activity',
            field=models.ForeignKey(null=True, to='app.Activity'),
        ),
    ]
