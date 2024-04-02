from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Book
def index(request):
    context={
        "message":"ceci est un test d'injection de contexte",
        "userList":["Foo","BAR","BAZ"],
        "username":"Smith",
        "books": Book.objects.all()
        }
    template= loader.get_template('manga/index.html')
    return HttpResponse(template.render(context,request))
 