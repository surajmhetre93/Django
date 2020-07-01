from django.forms import ModelForm
from django.core import validators
from .models import Login

class Loginform(ModelForm):
    class Meta:
        model = Login
        fields = "__all__"