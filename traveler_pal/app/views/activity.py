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


def getAllActivities(request):
    """
    渲染所有的活动界面
    """
    activities = Activity.objects.all()
    content = {
        "active": "activity",
        "activities": activities
    }
    csrfContext = RequestContext(request, content)
    return render_to_response("activities.html", csrfContext)


def getActivityInfo(request, activity_id):
    username = request.session.get('username', '')
    activity = Activity.objects.get(pk=activity_id)

    content = {
        "active": "activity",
        "activity": activity
    }
    csrfContext = RequestContext(request, content)
    return render_to_response("activity_info.html", csrfContext)


@login_required
def addActivity(request):
    """
    发起活动
    """
    if request.method == "POST":
        uname = request.POST.get('name', '')
        ustartDateTime = request.POST.get('startDateTime', '')
        uendDateTime = request.POST.get('endDateTime', '')
        scenerys = request.POST.getlist('scenery', '')
        uintroduction = request.POST.get('introduction', '')

        ulaunchedDateTime = time.strftime('%Y-%m-%d', time.localtime(time.time()))

        usponsor = request.session.get('username', '')

        newActivity = Activity.objects.create(
            name=uname,
            launchedDateTime=ulaunchedDateTime,
            startDateTime=ustartDateTime,
            endDateTime=uendDateTime,
            introduction=uintroduction,
            sponsor=usponsor,
        )
        newActivity.save()

        for scenery in scenerys:
            newScenery, isCreated = Scenery.objects.get_or_create(name=scenery)

            newActivityScenery = ActivityScenery(
                activity=newActivity,
                scenery=newScenery
            )
            newActivityScenery.save()

        data = {"status": 1}
        return HttpResponse(json.dumps(data, ensure_ascii=False))


def joinActivity(request):
    if request.method == "POST":
        activity_id = request.POST.get('activity_id', '')
        toJoinAct = Activity.objects.get(pk=activity_id)
        username = request.session['username']

        curPerson = Person.objects.get(username=username)

        try:
            newPersonActivity = PersonActivity(
                person=curPerson,
                activity=toJoinAct,
                joinedDateTime=Utils.getCurDateTime()
            )
            newPersonActivity.save()

            data = {"status": 1}
        except:
            data = {"status": 0}

        return HttpResponse(json.dumps(data, ensure_ascii=False))


@login_required
def delActivity(request):
    if request.POST:
        id = request.POST.get('activity_id', '')
        toDelActivity = Activity.objects.get(pk=id)
        toDelActivity.delete()


def getHotActivities(request):
    """
    依赖于多少个人参与了这个活动
    """
    leastSizeAsHot = 3
    hotActivities = filter(
        lambda activity: len(activity.person_set.all()) > 3,
        Activity.objects.all())

    return HttpResponse(json.dumps(
        {'hotActivities': map(Utils.toJSON, hotActivities)}
    ), ensure_ascii=False)
