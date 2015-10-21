"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),

    url(r'^u/(?P<username>\w+)/$', views.getUserProfile, name="user-profile"),

    url(r'^activity/$', views.getAllActivities, name="all-activities"),
    url(r'^activity/(?P<activity_id>[0-9]+)/$', views.getActivityInfo, name="activity-info"),
    url(r'^scenery/$', views.getAllScenery, name="all-scenery"),
    url(r'^scenery/(?P<scenery_id>[0-9]+)/$', views.getSceneryInfo, name="scenery-info"),

    url(r'^reg/$', views.register, name="register"),
    url(r'^login/$', views.login, name="login"),
    url(r'^logout/$', views.logout, name="logout"),
    url(r'^reset-password/$', views.resetPassword, name="reset-password"),

    url(r'^u/(?P<user_id>[0-9]+)/update/$', views.updateProfile, name="update profile"),
    url(r'^u/(?P<user_id>[0-9]+)/comment/$', views.getUserComments, name="user comments"),

    url(r'^scenery/(?P<scenery_id>[0-9]+)/comment/$', views.getSceneryComments, name="scenery comments"),

]
