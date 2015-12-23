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



def getAllScenery(request):
    """
    所有景点
    """
    limit = 5
    allScenery = Scenery.objects.all()
    paginator = Paginator(allScenery, limit)
    page = request.GET.get('page')
    try:
        allScenery = paginator.page(page)
    except EmptyPage:
        allScenery = paginator.page(paginator.num_pages)
    except:
        allScenery = paginator.page(1)
    content = {
        "active": "scenery",
        "allScenery": allScenery
    }
    csrfContext = RequestContext(request, content)
    return render_to_response("scenery.html", csrfContext)

def searchScenery(request):
    """
    search secnery all
    """
    limit = 5
    s = request.GET.get("name")
    allScenery = Scenery.objects.filter(name__contains=s)
    paginator = Paginator(allScenery, limit)
    page = request.GET.get('page')
    try:
        allScenery = paginator.page(page)
    except EmptyPage:
        allScenery = paginator.page(paginator.num_pages)
    except:
        allScenery = paginator.page(1)
    content = {
        "active": "scenery",
        "allScenery": allScenery
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
    strategy = Strategy.objects.filter(scenerys=scenery)
    activity = Activity.objects.filter(scenerys=scenery)
    content = RequestContext(request, {
        "active": "scenery",
        "scenery": scenery,
        "strategy": strategy,
        "activity": activity

    })
    csrfContext = RequestContext(request, content)
    return render_to_response("scenery_info.html", csrfContext)


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
