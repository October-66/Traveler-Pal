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
        return render_to_response("profile/slider-show.html", csrfContext)

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


def getactivity(request):
    pass




def getscenery(request):
    pass


def getjournal(request):
    pass

def getuser(request):
    pass



