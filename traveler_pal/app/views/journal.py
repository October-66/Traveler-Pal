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


@login_required
def addJournal(request):
    if request.POST:
        username = request.session.get('username')
        assert username
        title = request.POST.get('title')
        content = request.POST.get('content')
        activity_id = request.POST.get('activity_id')
        Journal.objects.create(
            person=Person.objects.get(username=username),
            title=title,
            content=content,
            activity=Activity.objects.get(pk=activity_id),
        ).save()


@login_required
def delJournal(request):
    if request.POST:
        id = request.POST.get('journal_id', '')
        Journal.objects.get(pk=id).delete()


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


@login_required
def delComment(request):
    if request.POST:
        Comment.objects.get(pk=request.POST['comment_id']).delete()
        return HttpResponse(json.dump({"status": 1}))


@login_required
def addStrategy(request):
    newStrategy = Strategy.objects.create(

    )
