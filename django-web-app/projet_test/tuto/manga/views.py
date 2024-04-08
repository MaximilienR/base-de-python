from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.template import loader
from .models import Book,Author
from .forms import SomeForm,BookForm

def index(request):
    context={
        "message":"ceci est un test d'injection de contexte",
        "userList":["Foo","BAR","BAZ"],
        "username":"Smith",
        }
    template= loader.get_template('manga/index.html')
    return HttpResponse(template.render(context,request))

def add(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        
        if  form.is_valid():
                form.save()
                return redirect('manga:index')
    else:
        form = BookForm()
        
    return render(request, "manga/book-form.html", {"form": form})



def show(request,book_id):
     context={"book": get_object_or_404(Book,pk=book_id)}
     return render(request,"manga/show.html",context)
 
 
def edit(request):
    book=Book.objects.get(title="random")
    book.title="db super"
    book.save()
    return redirect('manga:index')

def remove(request,book_id):
    book=Book.objects.get(pk=book_id)
    book.delete()
    return redirect("manga:index")

def book(request):
    context={
         "books": Book.objects.all().order_by("title")
        }
    template= loader.get_template('manga/book.html')
    return HttpResponse(template.render(context,request))

def form(request):     
    if request.method == 'POST':
     # créer une instance de notre formulaire et le remplir avec les données POST
        print('Les données POST sont : ', request.POST)
        form = SomeForm(request.POST)

        if form.is_valid():
            return redirect("manga.index")
         

        
    else:
 # ceci doit être une requête GET, donc créer un formulaire vide
        form = SomeForm()

    return render(request,
        'manga/form.html',
        {'form': form})

