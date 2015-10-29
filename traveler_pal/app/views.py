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
        return render(request, 'index.html')


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


def getAllActivities(request):
    activities = Activity.objects.all()
    context = RequestContext(request, {
        "activities": activities,
    })
    return HttpResponse("all act")


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


def delActivity(request, activity_id):
    toDelActivity = Activity.objects.get(pk=activity_id)
    toDelActivity.delete()


def getAllScenery(request):
    allScenery = Scenery.objects.all()
    context = RequestContext(request, {
        "allScenery": allScenery,
    })
    return HttpResponse("all scenery")


def getSceneryInfo(request, scenery_id):
    scenery = Scenery.objects.get(pk=scenery_id)
    context = RequestContext(request, {
        "scenery": scenery,
    })
    return HttpResponse("scenery info")


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
