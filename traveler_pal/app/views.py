from django.shortcuts import render
from django.http import *


# Create your views here.

def index(request):
    return render(request, 'index.html', {
        'test': '123test'
    })


def getUserProfile(request, user_id):
    return HttpResponse("User id: %s" % user_id)


def getActivityInfo(request, activity_id):
    return HttpResponse("act info")


def getAllActivities(request):
    return HttpResponse("all act")


def getAllScenery(request):
    return HttpResponse("all scenery")


def getSceneryInfo(request, scenery_id):
    return HttpResponse("scenery info")

