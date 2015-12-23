#!/usr/bin/env python
#coding:utf-8
import re
from django import template

register = template.Library()

def cut_images(value):

    value = value.replace(r'<img', '<h')

    return value

register.filter('cut_images', cut_images)