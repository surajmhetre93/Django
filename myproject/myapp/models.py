from django.db import models
from django import forms
from django.core import validators

# Create your models here.
class Login(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=50, validators = [validators.MinLengthValidator(5, "Enter min 5 characters")])

    def __str__(self):
        return self.name

class Session(models.Model):
    session = models.CharField(max_length = 30, unique = True)

    def __str__(self):
        return self.session

class Student(models.Model):
    name = models.CharField(max_length = 30, unique = False)
    session = models.ForeignKey("Session",on_delete=models.PROTECT)

    def __str__(self):
        return self.name

