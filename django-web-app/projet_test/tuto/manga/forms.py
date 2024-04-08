from django import forms
from .models import Author,Book

class SomeForm(forms.Form):
    email = forms.EmailField(label="email "  )
    password=forms.CharField(label="mot de passe", widget=forms.PasswordInput,required=True)
    my_checkbox = forms.BooleanField(label="je ne suis pas un robot", widget=forms.CheckboxInput,required=True)
    
class BookForm(forms.ModelForm):
    author=forms.ModelChoiceField(queryset=Author.objects.all(),label='Auteur')
    class Meta:
        model =Book
        fields =['title','author','quantity']
        labels= {'title': 'Titre','quantity':'Quantité'}