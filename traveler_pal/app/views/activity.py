# encoding: utf-8
from django.contrib import auth
from django.contrib.auth.decorators import *
from django.contrib.auth.models import User
from django.shortcuts import *
from django.http import *
from django.core.paginator import *
from django.core.mail import send_mail

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
    limit  = 5
    activities = Activity.objects.order_by("-id").all()
    paginator = Paginator(activities, limit)
    page = request.GET.get('page')
    try:
        activities = paginator.page(page)
    except EmptyPage:
        activities = paginator.page(paginator.num_pages)
    except:
        activities = paginator.page(1)
    content = {
        "active": "activity",
        "activities": activities
    }
    csrfContext = RequestContext(request, content)
    return render_to_response("activities.html", csrfContext)

def searchActivity(request):
    """
    search activity
    """
    s = request.GET.get('name')

    limit  = 5
    activities = Activity.objects.filter(name__contains=s)
    paginator = Paginator(activities, limit)
    page = request.GET.get('page')
    try:
        activities = paginator.page(page)
    except EmptyPage:
        activities = paginator.page(paginator.num_pages)
    except:
        activities = paginator.page(1)
    content = {
        "active": "activity",
        "activities": activities
    }
    csrfContext = RequestContext(request, content)
    return render_to_response("activities.html", csrfContext)


def getActivityInfo(request, activity_id):
    username = request.session.get('username', '')
    activity = Activity.objects.get(pk=activity_id)
    joinpeople = PersonActivity.objects.filter(activity=activity)
    scenery = Scenery.objects.order_by("-id").all()[:5]
    print joinpeople
    content = {
        "active": "activity",
        "activity": activity,
        "joinpeople": joinpeople,
        "scenery": scenery
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
        username = request.user

        curPerson = Person.objects.get(username=username)
        print "person name: ", curPerson.username
        try:
            if len(PersonActivity.objects.filter(person=curPerson).filter(activity=toJoinAct)) != 0:
                data = {"status": -1}
            else:
                newPersonActivity = PersonActivity(
                    person=curPerson,
                    activity=toJoinAct,
                    joinedDateTime=Utils.getCurDateTime()
                )
                newPersonActivity.save()

                data = {"status": 1}
        except:
            data = {"status": 0}
        # send mail
        joinpeople = PersonActivity.objects.filter(activity=toJoinAct)
        to_email = list()
        for t in joinpeople:
            to_email.append(t.person.email)
        send_mail('subject', 'message', 'ysbinang@qq.com', to_email,fail_silently=False)
        return HttpResponse(json.dumps(data, ensure_ascii=False))


@login_required
def delActivity(request):
    if request.POST:
        id = request.POST.get('activity_id', '')
        toDelActivity = Activity.objects.get(pk=id)
        toDelActivity.delete()
