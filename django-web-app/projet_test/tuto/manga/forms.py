from django import forms

class SomeForm(forms.Form):
    email = forms.EmailField(label="email "  )
    password=forms.CharField(label="mot de passe", widget=forms.PasswordInput,required=True)
    my_checkbox = forms.BooleanField(label="je ne suis pas un robot", widget=forms.CheckboxInput,required=True)