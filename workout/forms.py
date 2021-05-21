from django import forms
from .models import *
from django.forms import ModelForm


class AddMainWorkOut(ModelForm):
    class Meta:
        model = MainWorkout
        fields = ['goal_muscle','name','image','description']