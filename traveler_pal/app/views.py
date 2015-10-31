# encoding: utf-8
from django.contrib import auth
from django.contrib.auth.decorators import *
from django.contrib.auth.models import User
from django.shortcuts import *
from django.http import *
from .models import *
import json


# Create your views here.


def index(request):
    if request.method == 'GET':
       content = {
        "active": "index"
        }
    return render_to_response("index.html", content)

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
    activity = Activity.objects.get(pk=activity_id)
    context = RequestContext(request, {
        "activity": activity,

    })
    return HttpResponse("act info")

"""
所有活动
"""
def getAllActivities(request):
    activities = Activity.objects.all()
    content = {
        "active": "activity",
        "activities": activities
        }
    return render_to_response("activities.html", content)

def getPersonActivities(request, person_id):
    """
    find all personal activities according to person_id
    """
    reqPerson = Person.objects.get(pk=person_id)
    context = RequestContext(request, {
        "reqPerson": reqPerson,
    })
    return HttpResponse("")

"""
发起活动
"""
@login_required
def addActivity(request):
    """
    """
    if request.method == "POST":
        newActivity = Activity.objects.create(
            name=request.POST.get('name', ''),
            launchedDateTime=request.POST.get('launchedDateTime', ''),
            startDateTime=request.POST.get('startDateTime', ''),
            endDateTime=request.POST.get('endDateTime', ''),
            scenerys=request.POST.get('scenerys', '')
        )
        newActivity.save()

        data = {"status": 1}
        return HttpResponse(json.dumps(data, ensure_ascii=False))


@login_required
def delActivity(request, activity_id):
    toDelActivity = Activity.objects.get(pk=activity_id)
    toDelActivity.delete()


"""
所有景点
"""
def getAllScenery(request):
    allScenery = Scenery.objects.all()
    content = {
        "active": "scenery",
        "activities": allScenery
        }
    return render_to_response("scenery.html", content)


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
    return render_to_response("journal.html", content)


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
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
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
def getProfile(request, user_id):
    user = User.objects.all()
    content = {
        "user": user
    }
    return render_to_response("profile.html", content)

@login_required
def updateProfile(request):
    return None


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
        print request.POST
        return render(request, 'test.html')
