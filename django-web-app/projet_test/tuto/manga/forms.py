from django import forms

class SomeForm(forms.Form):
    nom = forms.CharField(required=True)
 