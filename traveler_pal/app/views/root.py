# encoding: utf-8
from django.contrib import auth
from django.contrib.auth.decorators import *
from django.contrib.auth.models import User
from django.shortcuts import *
from django.http import *
from django.core.paginator import *

from ..models import *
from .. import Utils

import json
import time
from django.views.decorators.csrf import *

def isroot(request):
    return request.session.get('isroot', '') == 'Y'

def isget(request):
    return request.method == "GET"

def ispost(request):
    return request.method == "POST"

@login_required
def getslider(request):
    if isroot(request) and isget(request):
        slider = Slider.objects.all()
        content = {
            "isroot": 'Y',
            "slider": slider
        }
        csrfContext = RequestContext(request, content)
        return render_to_response("profile/slider.html", csrfContext)

def addslider(request):
    if isroot(request) and ispost(request):
        title = request.POST['title']
        sliderImg = request.FILES['sliderImg']


        newSlider = Slider.objects.create(
            title = title,
            sliderImg = sliderImg
            )

        return HttpResponseRedirect('/u/slmanage/')

def updateslider(request):
    if isroot(request) and ispost(request):
        uid = request.POST['id']
        title = request.POST['title']
        sliderImg = request.FILES['sliderImg']

        newSlider = Slider(
            id = uid,
            title = title,
            sliderImg = sliderImg
            )
        newSlider.save()

        return HttpResponseRedirect('/u/slmanage')

@csrf_exempt
def deleteslider(request):
    if isroot(request) and ispost(request):
        uid = request.POST['id']
        slider = Slider.objects.get(pk=uid)
        slider.delete();
        return HttpResponseRedirect('/u/slmanage/')

@csrf_exempt
def getactivity(request):
    if request.POST:
        if not Person.objects.get(username=request.session['username']).isroot:
            return HttpResponseRedirect("/")
        if request.POST:
            toDelScry = Activity.objects.get(pk=request.POST["activity_id"])
            toDelScry.delete()
            data = {"status": 1}
            return HttpResponse(json.dumps(data, ensure_ascii=False))
    else:
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
            "isroot": 'Y',
            "active": "activity",
            "activities": activities
        }
        csrfContext = RequestContext(request, content)
        return render_to_response("profile/activity.html", csrfContext)




@csrf_exempt
def getscenery(request):
    if request.POST:
        if not Person.objects.get(username=request.session['username']).isroot:
            return HttpResponseRedirect("/")
        if request.POST:
            toDelScry = Scenery.objects.get(pk=request.POST["scenery_id"])
            toDelScry.delete()

            data = {"status": 1}
            return HttpResponse(json.dumps(data, ensure_ascii=False))
    else:
        """
        所有景点
        """
        limit = 5
        allScenery = Scenery.objects.all()
        paginator = Paginator(allScenery, limit)
        page = request.GET.get('page')
        try:
            allScenery = paginator.page(page)
        except EmptyPage:
            allScenery = paginator.page(paginator.num_pages)
        except:
            allScenery = paginator.page(1)
        content = {
            "isroot": 'Y',
            "active": "scenery",
            "allScenery": allScenery
        }
        csrfContext = RequestContext(request, content)
        return render_to_response("profile/scenery.html", csrfContext)

@csrf_exempt
def getstrategy(request):
    """
    所有攻略
    """
    if request.POST:
        if not Person.objects.get(username=request.session['username']).isroot:
            return HttpResponseRedirect("/")
        if request.POST:
            toDelStgy = Strategy.objects.get(pk=request.POST["strategy_id"])
            toDelStgy.delete()
            data = {"status": 1}
            return HttpResponse(json.dumps(data, ensure_ascii=False))

    else:
        limit = 5
        allStrategy = Strategy.objects.order_by("-id").all()
        paginator = Paginator(allStrategy, limit)
        page = request.GET.get('page')
        try:
            allStrategy = paginator.page(page)
        except EmptyPage:
            allStrategy = paginator.page(paginator.num_pages)
        except InvalidPage:
            allStrategy = paginator.page(1)
        content = {
            "isroot": 'Y',
            "allStrategy": allStrategy
        }
        csrfContext = RequestContext(request, content)
        return render_to_response("profile/strategy.html", csrfContext)

@csrf_exempt
def getuser(request):
    if request.POST:
        if not Person.objects.get(username=request.session['username']).isroot:
            return HttpResponseRedirect("/")
        if request.POST:
            person = Person.objects.get(pk=request.POST['user_id'])
            person.delete()
            data = {"status": 1}
            return HttpResponse(json.dumps(data, ensure_ascii=False))
    else:
        limit = 5
        allUser = Person.objects.all()
        paginator = Paginator(allUser, limit)
        page = request.GET.get('page')
        try:
            allUser = paginator.page(page)
        except EmptyPage:
            allUser = paginator.page(paginator.num_pages)
        except InvalidPage:
            allUser = paginator.page(1)
        content = {
            "isroot": 'Y',
            "allUser": allUser
        }
        csrfContext = RequestContext(request, content)
        return render_to_response("profile/user.html", csrfContext)



