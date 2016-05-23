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

class SpeakerForm(forms.Form):
    DEGREES = (
        ('Doc', 'Doctor'),
        ('Lic', 'Licenciado'),
        ('Ing', 'Ingeniero'),
        ('MC', 'Maestro en Ciencias')
    )
    Degree = forms.ChoiceField(choices = DEGREES)
    Name = forms.CharField()
    Last_Name = forms.CharField()
    Picture = forms.ImageField()

class ConferenceForm(forms.Form):
    Title = forms.CharField()
    Description = forms.CharField()
    Speaker = forms.ModelChoiceField(Speaker.objects, empty_label = "Select Speaker ")
    Date = forms.DateField()
    Time = forms.TimeField()
    Image = forms.ImageField()

class StaffForm(forms.Form):
    Name = forms.CharField()
    Phone = forms.IntegerField()
    Task = forms.CharField()

class MembersForm(UserCreationForm):
    STATUS = (
        ('AD', 'Administrator'),
        ('AC', 'Assistance Coordinator'),
        ('PC', 'Presentations Coordinator'),
        ('SC', 'Staff Coordinator'),
        )
    Position = forms.ChoiceField(choices = STATUS)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'is_superuser')
