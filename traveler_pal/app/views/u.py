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
from . import strategy



class TestUEditorForm(forms.Form):
    content = UEditorField(u"", initial="abc")

def resetPassword(request):
    pass

@login_required
def getProfile(request):
    username = request.session.get('username', '')
    person = Person.objects.get(username=username)
    isroot = request.session.get('isroot', '')
    content = {
        "person": person,
        "isroot": isroot
    }
    csrfContext = RequestContext(request, content)
    return render_to_response("profile/profile.html", csrfContext)

def getPerson(request):
    username = request.session['username']
    assert username
    return Person.objects.get(username=username)


@login_required
def getUserProfile(request, username):
    """
    渲染用户信息界面
    """
    if request.method == 'GET':
        user = Person.objects.get(username=username)
        context = RequestContext(request, {
            "username": user.username,
            "email": user.email,
            "interest": user.interest,
            "gender": user.gender,
            "activitys": user.activitys,
            "scenerys": user.scenerys,
        })
    return HttpResponse("User id: %s" % username)


@login_required
def postStrategy(request):
    """
    发表攻略
    """
    if request.method == "GET":
        username = request.session.get('username', '')
        form = TestUEditorForm()
        content = {
            "username": username,
            "form": form
        }
        csrfContext = RequestContext(request, content)
        return render_to_response("profile/post.html", csrfContext)
    else:
        username=request.session.get('username')
        scenery=request.POST.get("scenery-tag")
        newStrategy = Strategy.objects.create(
            person=Person.objects.get(username=username),
            title=request.POST.get('title'),
            content=request.POST.get('content'),
            postDateTime=request.POST.get('dateTime'),
            scenerys=Scenery.objects.get_or_create(name=scenery)[0]
        )
        print newStrategy
        newStrategy.save()
        
        data = {"status": 1}
        return HttpResponse(json.dumps(data, ensure_ascii=False))


@login_required
def getPersonActivities(request):
    """
    refer to ManyToManyField doc
    """
    if request.method == "GET":
        username = request.session['username']
        assert username
        reqPerson = Person.objects.get(username=username)
        activities = [a.name for a in list(reqPerson.activitys.all())]
        content = {
        "active": "activity",
        "activities": activities
    }
    csrfContext = RequestContext(request, content)
    return render_to_response("joined-activities.html", csrfContext)


@login_required
def updateProfile(request):
    print "updateprofile"
    if request.method == "GET":
        content = {
        # "active": "activity",
        # "activities": activities
        }
        csrfContext = RequestContext(request, content)
        return render_to_response("profile/update.html", csrfContext)
    else:
        username = request.session['username']
        print username
        reqPerson = Person.objects.get(username=username)
        reqPerson.interest = request.POST.get("interest")
        print "reqPerson.interest: ", reqPerson.interest
        reqPerson.save()
        content = {
        }
        csrfContext = RequestContext(request, content)
        return render_to_response("profile/update.html", csrfContext)



@login_required
def changePw(request):
    pass
