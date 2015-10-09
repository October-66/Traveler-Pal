from django.contrib import auth
from django.contrib.auth.decorators import *
from django.contrib.auth.models import User
from django.shortcuts import *
from django.http import *
from .forms import *


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


def register(request):
    if request.method == 'GET':
        form = RegForm()
        return render_to_response('register.html', RequestContext(request, {'form': form}))
    else:
        form = RegForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username', '')
            email = request.POST.get('email', '')
            password = request.POST.get('password', '')
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
            )
        return HttpResponseRedirect('/')


def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render_to_response('login.html', RequestContext(request, {'form': form}))
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return HttpResponse("auth succeed")
            else:
                # auth failed
                return HttpResponse("auth failed")


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
