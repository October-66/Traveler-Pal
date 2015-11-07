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

def getAllJournal(request):
    allScenery = Journal.objects.all()
    content = {
        "active": "journal",
        "activities": allScenery
    }
    csrfContext = RequestContext(request, content)
    return render_to_response("journal.html", csrfContext)

def addJournal(request):
    pass


def delJournal(request, journal_id):
    pass


def getHotJournal(request):
    """
    依赖于多少个人访问过这个日志
    """

def getAllStrategy(request):
    """
    所有攻略
    """
    allStrategy = Strategy.objects.all()
    pass


def delComment(request, comment_id):
    Comment.objects.get(pk=comment_id).delete()
    return HttpResponse(json.dump({"status": 1}))


def addStrategy(request):
    newStrategy = Strategy.objects.create(

    )