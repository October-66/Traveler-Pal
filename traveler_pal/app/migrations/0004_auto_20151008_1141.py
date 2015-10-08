# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_activityuser_joineddate'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('username', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=128)),
                ('password', models.CharField(max_length=128)),
                ('interest', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='activity',
            old_name='members',
            new_name='users',
        ),
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
        migrations.RemoveField(
            model_name='user',
            name='password',
        ),
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
        migrations.AddField(
            model_name='activity',
            name='scenerys',
            field=models.ManyToManyField(to='app.Scenery', through='app.ActivityScenery'),
        ),
        migrations.AddField(
            model_name='activityscenery',
            name='activity',
            field=models.ForeignKey(null=True, to='app.Activity'),
        ),
        migrations.AddField(
            model_name='activityscenery',
            name='scenery',
            field=models.ForeignKey(null=True, to='app.Scenery'),
        ),
        migrations.AddField(
            model_name='comment',
            name='content',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='journal',
            name='content',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='journal',
            name='title',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='scenery',
            name='comments',
            field=models.ManyToManyField(to='app.Comment', through='app.SceneryComment'),
        ),
        migrations.AddField(
            model_name='scenery',
            name='name',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='scenery',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='scenerycomment',
            name='comment',
            field=models.ForeignKey(null=True, to='app.Comment'),
        ),
        migrations.AddField(
            model_name='scenerycomment',
            name='scenery',
            field=models.ForeignKey(null=True, to='app.Scenery'),
        ),
        migrations.AddField(
            model_name='user',
            name='comments',
            field=models.ManyToManyField(to='app.Comment', through='app.UserComment'),
        ),
        migrations.AddField(
            model_name='user',
            name='journals',
            field=models.ManyToManyField(to='app.Journal', through='app.UserJournal'),
        ),
        migrations.AddField(
            model_name='usercomment',
            name='Comment',
            field=models.ForeignKey(null=True, to='app.Comment'),
        ),
        migrations.AddField(
            model_name='usercomment',
            name='user',
            field=models.ForeignKey(null=True, to='app.User'),
        ),
        migrations.AddField(
            model_name='userjournal',
            name='journal',
            field=models.ForeignKey(null=True, to='app.Journal'),
        ),
        migrations.AddField(
            model_name='userjournal',
            name='user',
            field=models.ForeignKey(null=True, to='app.User'),
        ),
        migrations.AlterField(
            model_name='activityuser',
            name='activity',
            field=models.ForeignKey(null=True, to='app.Activity'),
        ),
        migrations.AlterField(
            model_name='activityuser',
            name='user',
            field=models.ForeignKey(null=True, to='app.User'),
        ),
        migrations.AddField(
            model_name='user',
            name='info',
            field=models.OneToOneField(null=True, to='app.UserInfo'),
        ),
    ]
