# -*- coding: utf-8 -*-
from django.template import loader, Context, RequestContext, Template
from django.http import HttpResponse, Http404
from models import *
from core.models import Node
from django.conf import settings
from django.shortcuts import redirect


def view(request, node):
    t = loader.get_template("department/view.html")
    c = RequestContext(request, {'node': node})
    return HttpResponse(t.render(c))

def edit(request, node):
    if request.method == 'POST':
        node.title = request.POST['title']
        node.text = request.POST['text']
        node.status = 'status' in request.POST
        node.show_rightmenu = 'show_rightmenu' in request.POST
        node.save(request.user)

    t = loader.get_template("department/edit.html")
    c = RequestContext(request, {'node': node, 'mode': 'edit'})
    return HttpResponse(t.render(c))


def history(request, node):
    a = History.objects.filter(node = node)
    t = loader.get_template("department/history.html")
    c = RequestContext(request, {'node': node, 'mode': 'history', 'list': a})
    return HttpResponse(t.render(c))


def restore(request, node):
    if request.method == 'GET':
        a = History.objects.get(id = int(request.GET['id']))
        node.text = a.page
        node.save(request.user)



    t = loader.get_template("department/view.html")
    c = RequestContext(request, {'node': node})
    return HttpResponse(t.render(c))