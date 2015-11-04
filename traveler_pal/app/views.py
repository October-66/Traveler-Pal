# encoding: utf-8
from django.contrib import auth
from django.contrib.auth.decorators import *
from django.contrib.auth.models import User
from django.shortcuts import *
from django.http import *
from .models import *

import json
import time

from  DjangoUeditor.forms import UEditorField
from django import forms
# Create your views here.

class TestUEditorForm(forms.Form):
    content=UEditorField(u"",initial="abc")


def index(request):
    if request.method == 'GET':
        username = request.session.get('username', '')
        content = {
            "active": "index",
            "username": username,

        }
        csrfContext = RequestContext(request, content)
        return render_to_response("index.html", csrfContext)


@login_required
def getUserProfile(request, username):
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


def getActivityInfo(request, activity_id):
    username = request.session.get('username', '')
    content = {
            "active": "activity",
            "username": username,
        }
    csrfContext = RequestContext(request, content)
    return render_to_response("activity_info.html", csrfContext)
    '''
    activity = Activity.objects.get(pk=activity_id)
    context = RequestContext(request, {
        "activity": activity,

    })
    return HttpResponse("act info")
    '''


def getAllActivities(request):
    """
    所有活动
    """
    activities = Activity.objects.all()
    content = {
        "active": "activity",
        "activities": activities
    }
    csrfContext = RequestContext(request, content)
    return render_to_response("activities.html", csrfContext)


def getRecentActivities(request):
    rcntActivitiesSize = 5
    rcntActivities = Activity.objects.order_by("launchedDateTime").all()[:rcntActivitiesSize]
    content = {
        "rcntActivities": rcntActivities,
    }
    return render_to_response("", content)

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
def addActivity(request):
    """
    发起活动
    """
    if request.method == "POST":
        uname = request.POST.get('name', '')
        ustartDateTime = request.POST.get('startDateTime', '')
        uendDateTime = request.POST.get('endDateTime', '')
        uscenery = request.POST.get('scenery', '')
        uintroduction = request.POST.get('uintroduction', '')

        ulaunchedDateTime = time.strftime('%Y-%m-%d',time.localtime(time.time()))


        newActivity = Activity.objects.create(
            name = uname,
            launchedDateTime = ulaunchedDateTime,
            startDateTime = ustartDateTime,
            endDateTime = uendDateTime,
        )
        
        for uscenery_list in uscenery:
            newScenery = Scenery.objects.get_or_create(name = uscenery_list)[0]
            
            newActivityScenery = ActivityScenery(
                activity = newActivity,
                scenery = newScenery
                )
            newActivityScenery.save()

        data = {"status": 1}
        return HttpResponse(json.dumps(data, ensure_ascii=False))


@login_required
def delActivity(request, activity_id):
    toDelActivity = Activity.objects.get(pk=activity_id)
    toDelActivity.delete()


def addJournal(request):
    pass

def delJournal(request, journal_id):
    pass

"""
所有景点
"""


def getAllScenery(request):
    allScenery = Scenery.objects.all()
    content = {
        "active": "scenery",
        "activities": allScenery
    }
    csrfContext = RequestContext(request, content)
    return render_to_response("scenery.html", csrfContext)

def getHotScenery(request):
    """
    依赖于多少个人游览过这个风景
    """

def getHotActivities(request):
    """
    依赖于多少个人参与了这个活动
    """

def getHotJournal(request):
    """
    依赖于多少个人访问过这个日志
    """



def getSceneryInfo(request, scenery_id):
    scenery = Scenery.objects.get(pk=scenery_id)
    context = RequestContext(request, {
        "scenery": scenery,
    })
    return HttpResponse("scenery info")


"""
所有攻略
"""


def getAllJournal(request):
    allScenery = Journal.objects.all()
    content = {
        "active": "journal",
        "activities": allScenery
    }
    csrfContext = RequestContext(request, content)
    return render_to_response("journal.html", csrfContext)


def register(request):
    if request.method == 'GET':
        pass
    else:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        repassword = request.POST.get('repassword', '')
        email = request.POST.get('email', '')

        if password == repassword:

            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
            )
            data = {"status": 1}
            return HttpResponse(json.dumps(data, ensure_ascii=False))
        else:
            data = {"status": -3}
            return HttpResponse(json.dumps(data, ensure_ascii=False))


def login(request):
    if request.session.get('username', ''):
        return HttpResponseRedirect('/')

    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            request.session['username'] = username
            data = {"status": 1}
            return HttpResponse(json.dumps(data, ensure_ascii=False))
        else:
            data = {"status": 0}
            return HttpResponse(json.dumps(data, ensure_ascii=False))


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")


def resetPassword(request):
    return None


@login_required
def getProfile(request):
    username = request.session.get('username', '')
    content = {
        "username": username
    }
    csrfContext = RequestContext(request, content)
    return render_to_response("profile/profile.html", csrfContext)


@login_required
def updateProfile(request):
    return None

@login_required
def postJournal(request):
    if request.method == "GET":
        username = request.session.get('username', '')
        form = TestUEditorForm()
        content = {
            "username": username,
            "form": form
        }
        csrfContext = RequestContext(request, content)
        return render_to_response("profile/post.html", csrfContext)
    elif request.method == "POST":
        pass



def getPersonActivities(request, person_id):
    """
    refer to ManyToManyField doc
    """
    if request.method == "GET":
        reqPerson = Person.objects.get(pk=person_id)
        activities = Activity.objects.all()
        context = RequestContext(request, {
            "activities": activities,
        })
        return HttpResponse("activities")

def addComment(request):
    """
    关键的信息是用户的信息
    """
    pass

def delComment(request):
    pass


def getUserComments(request, user_id):
    return None


def getSceneryComments(request, scenery_id):
    return None


"""
测试交互数据使用
"""


def test(request):
    if request.method == "GET":
        return render(request, 'test.html')

    else:
        return render(request, 'test.html')
