from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Book

def index(request):
    context={
        "message":"ceci est un test d'injection de contexte",
        "userList":["Foo","BAR","BAZ"],
        "username":"Smith",
        }
    template= loader.get_template('manga/index.html')
    return HttpResponse(template.render(context,request))
 
def show(request,book_id):
     context={"book": get_object_or_404(Book,pk=book_id)}
     return render(request,"manga/show.html",context)
 
def book(request):
    context={
         "books": Book.objects.all().order_by("title")
        }
    template= loader.get_template('manga/book.html')
    return HttpResponse(template.render(context,request))
 