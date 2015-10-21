from django.contrib import auth
from django.contrib.auth.decorators import *
from django.contrib.auth.models import User
from django.shortcuts import *
from django.http import *
from .forms import *

import json

# Create your views here.


def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')


def getUserProfile(request, username):

    return HttpResponse("User id: %s" % username)


def getActivityInfo(request, activity_id):
    return HttpResponse("act info")


def getAllActivities(request):
    return HttpResponse("all act")


def getAllScenery(request):
    return HttpResponse("all scenery")


def getSceneryInfo(request, scenery_id):
    return HttpResponse("scenery info")

def register(request):
    if request.method == 'GET':
        form = RegForm()
        return render_to_response('register.html', RequestContext(request, {'form': form}))
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


def getUserComments(request, user_id):
    return None


def getSceneryComments(request, scenery_id):
    return None
