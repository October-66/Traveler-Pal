# encoding: utf-8
from django.contrib.auth.decorators import *
from django.core.paginator import *
from django.shortcuts import render_to_response
from django.template import RequestContext

from ..models import *

def getAllStrategy(request):
    """
    所有攻略
    """
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

def delStrategy(request):

    if not Person.objects.get(username=request.session['username']).isroot:
        return HttpResponseRedirect("/")
    if request.POST:
        toDelStgy = Strategy.objects.get(pk=request.POST["strategy_id"])
        toDelStgy.delete()


    content = {
        "active": "strategy",
        "allStrategy": allStrategy
    }
    csrfContent = RequestContext(request, content)

    return render_to_response("strategy.html", csrfContent)

@login_required
def getPostedStrategy(request):
    username = request.session['username']
    allStrategy = Strategy.objects.filter(person=Person.objects.get(username=username))
    return render_to_response("posted-strategy.html", RequestContext(request, {
        "active": "posted-strategy",
        "allStrategy": allStrategy
    }))

def getOneStrategy(request, strategy_id):
    strategy = Strategy.objects.get(pk=strategy_id)

    content = {
        "active": "strategy",
        "strategy": strategy
    }

    csrfContent = RequestContext(request, content)

    return render_to_response("strategy_info.html", csrfContent)

