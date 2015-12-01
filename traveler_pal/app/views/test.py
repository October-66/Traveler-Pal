# encoding: utf-8
from django.contrib import auth
from django.contrib.auth.decorators import *
from django.contrib.auth.models import User
from django.shortcuts import *
from django.http import *
from django.core.mail import send_mail
from ..models import *
from .. import Utils

import json
import time

from  DjangoUeditor.forms import UEditorField
from django import forms

"""
测试交互数据使用
"""


def test(request):
    if request.method == "GET":
        send_mail('subject', 'message', 'ysbinang@qq.com', ['admin@rccoder.net','rccoder@foxmail.com'],fail_silently=False)
        return render(request, 'test.html')

    else:
        return render(request, 'test.html')
