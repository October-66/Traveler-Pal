from django.contrib import auth
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
        return render_to_response('after reg')


def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render_to_response('login.html', RequestContext(request, {'form': form}))
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST.get('email', '')
            password = request.POST.get('password', '')
            user = auth.authenticate(email=email, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return render_to_response('after login page', RequestContext(request))
            else:
                pass  # auth failed


def logout(request):
    return None


def resetPassword(request):
    return None


def updateProfile(request):
    return None


def getUserComments(request, user_id):
    return None


def getSceneryComments(request, scenery_id):
    return None
