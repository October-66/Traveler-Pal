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

from  DjangoUeditor.forms import UEditorField
from django import forms

def activity(request):
    pass

def popular_activity(request):
    pass

def popular_scenery(request):
    pass

def popular_strategy(request):
    pass