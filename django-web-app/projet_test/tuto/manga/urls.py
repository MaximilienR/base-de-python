from django.urls import path
from . import views

app_name="manga"
urlpatterns = [
    path('',views.index, name='index'),
    path('<int:book_id>',views.show, name='show'),
    path('book',views.book,name='book'),
    path('ajouter-livre/',views.add,name='add'),
    path('modifierr-livre/<int:book_id>',views.edit,name='edit'),
    path('supprimer-livre/<int:book_id>',views.remove,name='delete'),
    path('form',views.form, name="form"),

]