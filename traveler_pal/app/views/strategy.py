# encoding: utf-8
from django.contrib.auth.decorators import *
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.shortcuts import render_to_response
from django.template import RequestContext

from ..models import *


def getAllStrategy(request):
    """
    所有攻略
    """
    limit = 5
    allStrategy = Strategy.objects.all()
    pagtor = Paginator(allStrategy, limit)
    page = request.GET.get('page')
    try:
        pagedStgy = pagtor.page(page)
    except EmptyPage:
        pagedStgy = pagtor.page(pagtor.num_pages)
    except InvalidPage:
        pagedStgy = pagtor.page(1)
    return render_to_response("strategy.html", RequestContext(request, {
        "active": "strategy",
        "allStrategy": pagedStgy
    }))

@login_required
def getPostedStrategy(request):
    username = request.session['username']
    strgySet = Strategy.objects.filter(person=Person.objects.get(username=username))
    # limit = 5
    # pagtor = Paginator(strgySet, limit)
    # page = request.GET.get('page')
    # try:
    #     pagedStgy = pagtor.page(page)
    # except EmptyPage:
    #     pagedStgy = pagtor.page(pagtor.num_pages)
    # except InvalidPage:
    #     pagedStgy = pagtor.page(1)
    # return render_to_response("posted-strategy.html", RequestContext(request, {
    #     "active": "posted-strategy",
    #     "allStrategy": pagedStgy
    # }))
    allStrategy = Strategy.objects.all()
    return render_to_response("posted-strategy.html", RequestContext(request, {
    "active": "posted-strategy",
    "allStrategy": allStrategy
    }))