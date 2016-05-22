from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Members, Speaker, Conference, Assistant ,Staff

class AssistantForm(forms.Form):
    Name = forms.CharField()
    Last_Name = forms.CharField()
    Age = forms.IntegerField()
    email = forms.EmailField()
