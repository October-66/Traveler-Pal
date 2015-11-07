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



def getAllScenery(request):
    """
    所有景点
    """
    allScenery = Scenery.objects.all()
    content = {
        "active": "scenery",
        "activities": allScenery
    }
    csrfContext = RequestContext(request, content)
    return render_to_response("scenery.html", csrfContext)


def toJSON(self):
    fields = []
    for field in self._meta.fields:
        fields.append(field.name)

    d = {}
    for attr in fields:
        d[attr] = getattr(self, attr)

    import json
    return json.dumps(d)

def getFuzzySearchScenerys(request, fuzzyQueryWord):
    """
    模糊查询景点
    """
    scenerys = Scenery.objects.filter(name__contains=fuzzyQueryWord)
    
    l=[]
    for x in scenerys:
        l.append(toJSON(x))
    print l
    return HttpResponse(json.dumps({'data_list':l}, ensure_ascii=False))


def getSceneryInfo(request, scenery_id):
    scenery = Scenery.objects.get(pk=scenery_id)
    context = RequestContext(request, {
        "scenery": scenery,
    })
    return HttpResponse("scenery info")


def getSceneryComments(request, scenery_id):
    if request.GET:
        commentSet = Scenery.objects.get(pk=scenery_id).comment_set.all()
        commentsJson = {}
        for comment in commentSet:
            commentsJson[comment.person.username] = comment.content
        return HttpResponse(json.dump(commentsJson))


def getHotScenery(request):
    """
    依赖于多少个人游览过这个风景
    """
    pass


def addCommentToScenery(request):
    sceneryName = request.session['scenery']
    assert sceneryName
    if request.POST:
        reqPerson = getPerson(request)
        Comment.objects.create(
            person=reqPerson,
            title=request.POST['title'],
            content=request.POST['content'],
            postDateTime=request.POST['postDateTime'],
            scenery=Scenery.objects.get(name=sceneryName)
        ).save()
        return HttpResponse(json.dump({"status": 1}))
