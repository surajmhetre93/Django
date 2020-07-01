from django.forms import ModelForm
from django.core import validators
from .models import BlogPost

class BlogPostForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = "__all__"