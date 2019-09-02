from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('login/index.html')
    context = {"login:_page": "active"}
    return HttpResponse(template.render(context))

def reset_pass(request):
    template = loader.get_template('login/reset-password.html')
    context = {"login:_page": "active"}
    return HttpResponse(template.render(context))