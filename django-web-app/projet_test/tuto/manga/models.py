from django.db import models
from django import forms

class Author(models.Model):
    name =models.CharField(max_length=40,unique=True)
    
    def __str__(self):
        return self.name
   

class Book(models.Model):
    title =models.CharField(max_length=32,unique=True)
    quantity=models.IntegerField(default=1)    
    author=models.ForeignKey(Author,on_delete=models.CASCADE)

class ContactForm(forms.Form):
    nom = forms.CharField(required=False)