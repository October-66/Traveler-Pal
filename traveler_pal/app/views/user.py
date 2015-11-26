# encoding: utf-8
from django.contrib import auth
from django.contrib.auth.decorators import *
from django.contrib.auth.models import *
from django.shortcuts import *
from django.http import *
from ..models import *
from .. import Utils

import json
import time

from  DjangoUeditor.forms import UEditorField
from django import forms

def register(request):
    if request.method == 'GET':
        pass
    else:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        repassword = request.POST.get('repassword', '')
        email = request.POST.get('email', '')

        if password == repassword:

            newUser = User.objects.create_user(
                username=username,
                email=email,
                password=password,
            )

            newPerson = Person.objects.create(
                user=newUser,
                username=username
            )
            data = {"status": 1}
            return HttpResponse(json.dumps(data, ensure_ascii=False))
        else:
            data = {"status": -3}
            return HttpResponse(json.dumps(data, ensure_ascii=False))


def login(request):
    if request.session.get('username', ''):
        return HttpResponseRedirect('/')

    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            request.session['username'] = username
            data = {"status": 1}
            return HttpResponse(json.dumps(data, ensure_ascii=False))
        else:
            data = {"status": 0}
            return HttpResponse(json.dumps(data, ensure_ascii=False))


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")
