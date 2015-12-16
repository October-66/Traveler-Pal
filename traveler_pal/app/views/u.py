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
    return None

@login_required
def getProfile(request):
    username = request.session.get('username', '')
    isroot = request.session.get('isroot', '')
    content = {
        "username": username,
        "isroot": isroot
    }
    csrfContext = RequestContext(request, content)
    return render_to_response("profile/profile.html", csrfContext)

def getPerson(request):
    username = request.session['username']
    assert username
    return Person.objects.get(username=username)


@login_required
def updateProfile(request):
    return None

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
        strategy.addStrategy(request)


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



def getPersonActivities(request, person_id):
    """
    find all personal activities according to person_id
    """
    reqPerson = Person.objects.get(pk=person_id)
    context = RequestContext(request, {
        "reqPerson": reqPerson,
    })
    return HttpResponse("")

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
        return HttpResponse(json.dump(activities))

@login_required
def updateProfile(request):
    if request.GET:
        return render_to_response("profile/update.html")
    if request.POST:
        username=request.session['username']
        reqPerson=Person.objects.get(username=username)
        reqPerson.interest=request.POST.get('interest')
        reqPerson.gender=request.POST.get('gender')

