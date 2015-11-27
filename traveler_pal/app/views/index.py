# encoding: utf-8
from django.contrib import auth
from django.contrib.auth.decorators import *
from django.contrib.auth.models import User
from django.shortcuts import *
from django.http import *
from ..models import *
from .. import Utils

import json
import time

from  DjangoUeditor.forms import UEditorField
from django import forms


def getRecentActivities():
    """
    get recent global activities
    return a object
    """
    rcntActivitiesSize = 5
    rcntActivities = Activity.objects.order_by("-id").all()[:rcntActivitiesSize]

    return rcntActivities

def getslider():
    """
    get the slider to show in index.html
    """
    return Slider.objects.all()

def index(request):
    """
    渲染主页
    """
    if request.method == 'GET':
        username = request.session.get('username', '')
        content = {
            "active": "index",
            "username": username,
            "recentactivity": getRecentActivities(),
            "slider": getslider,
        }
        csrfContext = RequestContext(request, content)
        return render_to_response("index.html", csrfContext)
