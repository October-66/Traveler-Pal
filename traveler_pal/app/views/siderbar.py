# encoding: utf-8
from django.contrib import auth
from django.contrib.auth.decorators import *
from django.contrib.auth.models import User
from django.shortcuts import *
from django.http import *
from django.core.paginator import *
from ..models import *
from .. import Utils

import json
import time

from  DjangoUeditor.forms import UEditorField
from django import forms


def activity(request):
    if request.session['username'] != '':
        size = 5
        person = Person.objects.get(username=request.session['username'])
        acts = person.activitys
        return HttpResponse(json.dumps(
                {'hotActivities': map(Utils.toJSON, acts)}
                , ensure_ascii=False))


def popular_activity(request):
    """
    依赖于多少个人参与了这个活动
    """
    leastSizeAsHot = 5
    hotActivities = list(Activity.objects.all())[-leastSizeAsHot:]

    for act in hotActivities:
        act.launchedDateTime = None
        act.startDateTime = None
        act.endDateTime = None
    return HttpResponse(json.dumps(
            {'hotActivities': map(Utils.toJSON, hotActivities)}
            , ensure_ascii=False))


def popular_scenery(request):
    size = 5
    hotScenerys = list(Scenery.objects.all())[-size:]

    return HttpResponse(json.dumps(
            {'hotScenerys': map(Utils.toJSON, hotScenerys)}
            , ensure_ascii=False))


def popular_strategy(request):
    size = 5
    hotStrategys = list(Strategy.objects.all())[-size:]
    for stgy in hotStrategys:
        stgy.postDateTime = None
    return HttpResponse(json.dumps(
            {'hotStrategys': map(Utils.toJSON, hotStrategys)}
            , ensure_ascii=False))
