from django.db import models
from django import forms
from django.core import validators

# Create your models here.
class BlogPost(models.Model):
    author_name = models.CharField(max_length=50)
    author_email = models.EmailField(max_length=50, unique=True)
    date_published = models.DateField()
    post_title = models.CharField(max_length=100)
    post_content = models.CharField(max_length=10000)
    
    def __str__(self):
        return self.post_title

