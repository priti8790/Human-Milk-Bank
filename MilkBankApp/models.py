from django.db import models

# Create your models here.

class Login(models.Model):
    username=models.CharField(max_length=25)
    password=models.CharField(max_length=15)