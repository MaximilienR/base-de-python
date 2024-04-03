from django.urls import path
from . import views

app_name="manga"
urlpatterns = [
    path('',views.index, name='index'),
    path('<int:book_id>',views.show, name='show'),
    path('book',views.book,name='book')
]