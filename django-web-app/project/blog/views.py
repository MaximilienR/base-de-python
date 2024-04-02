from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def about(request):
    return render(request,'about.html')

def register(request):
    if request.method=='POST':
        print("les donnes sont : ", request.POST)
    return render(request,
                  'register.html')