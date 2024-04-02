from django.db import models

class User(models.Model):
    mail=models.fields.EmailField(max_length=30)
    password=models.fields.CharField(max_length=20)
    