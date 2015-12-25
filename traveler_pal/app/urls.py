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
from django.contrib.staticfiles import views
from django.conf import settings

from .views import index
from .views import user
from .views import u
from .views import root
from .views import activity
from .views import scenery
from .views import strategy
from .views import siderbar
from .views import test

urlpatterns = [
    url(r'^$', index.index, name="index"),

    url(r'^activity/$', activity.getAllActivities, name="all-activities"),
    url(r'^activity/add/$', activity.addActivity, name="addActivity"),
    url(r'^activity/(?P<activity_id>[0-9]+)/$', activity.getActivityInfo, name="activity-info"),
    url(r'^activity/join/$', activity.joinActivity, name="activity-join"),
    url(r'^activity/s/$', activity.searchActivity, name="activity-search"),

    url(r'^scenery/$', scenery.getAllScenery, name="all-scenery"),
    url(r'^scenery/(?P<scenery_id>[0-9]+)/$', scenery.getSceneryInfo, name="scenery-info"),
    url(r'^scenery/search/(?P<fuzzyQueryWord>\w+)/$', scenery.getFuzzySearchScenerys, name="getFuzzySearchScenerys"),
    url(r'^scenery/s/$', scenery.searchScenery, name="scenery-search"),


    url(r'^strategy/$', strategy.getAllStrategy, name="all-strategy"),
    url(r'^strategy/(?P<strategy_id>[0-9]+)/$', strategy.getOneStrategy, name="one-strategy"),

    url(r'^reg/$', user.register, name="register"),
    url(r'^login/$', user.login, name="login"),
    url(r'^logout/$', user.logout, name="logout"),


    url(r'^u/reset-password/$', u.resetPassword, name="reset-password"),
    url(r'^u/update/$', u.updateProfile, name="update profile"),
    url(r'^u/post/$', u.postStrategy, name="post journal"),

    url(r'^u/slmanage/$', root.getslider, name="getslider"),
    url(r'^u/slmanage/add/$', root.addslider, name="addslider"),
    #url(r'^u/slmanage/update/$', root.updateslider, name="updateslider"),
    url(r'^u/slmanage/delete/$', root.deleteslider, name="deleteslider"),
    url(r'^u/acmanage/$', root.getactivity, name="getactivity"),
    url(r'^u/scmanage/$', root.getscenery, name="getscenery"),
    url(r'^u/jomanage/$', root.getstrategy, name="getjournal"),
    url(r'^u/usmanage/$', root.getuser, name="getuser"),

    # url(r'^u/(?P<username>\w+)/$', u.getUserProfile, name="user-profile"),

    url(r'^u/$', u.getProfile, name="get profile"),
    url(r'^u/activity/$', u.getPersonActivities),
    url(r'^u/post/list/$', strategy.getPostedStrategy, name="get all strategy"),

    url(r'^siderbar/activity/$', siderbar.activity),
    url(r'^siderbar/popular/activity/$', siderbar.popular_activity),
    url(r'^siderbar/popular/scenery/$', siderbar.popular_scenery),
    url(r'^siderbar/popular/strategy/$', siderbar.popular_strategy),

    url(r'^test/', test.test, name="test")

]

urlpatterns += [
    url(r'^static/(?P<path>.*)$', views.static.serve, {'document_root': settings.STATIC_ROOT}, name="static"),
    url(r'^media/(?P<path>.*)$', views.static.serve, {'document_root': settings.MEDIA_ROOT}, name="media")
]
