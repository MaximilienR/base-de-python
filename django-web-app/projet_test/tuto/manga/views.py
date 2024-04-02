from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    context={
        "message":"ceci est un test d'injection de contexte",
        "userList":["Foo","BAR","BAZ"],
        "username":"Smith"
        }
    template= loader.get_template('manga/index.html')
    return HttpResponse(template.render(context,request))
 