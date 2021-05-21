from django import forms
from django.forms import ModelForm
from .models import *


class Registration(forms.Form):
    user_name = forms.CharField(max_length=15, required=True)
    password = forms.CharField(max_length=20, required=True)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=20)
    age = forms.FloatField()
    is_superuser = forms.BooleanField()


class LogIn(forms.Form):
    user_name = forms.CharField(max_length=15, required=True)
    password = forms.CharField(widget=forms.PasswordInput())


class Posting(ModelForm):
    class Meta:
        model = Post
        fields = ['text', 'image']


class Commenting(forms.Form):
    text = forms.CharField(max_length=100, required=True, label='add comment')


class WriteArticle(ModelForm):
    class Meta:
        model = Article
        fields = ['text']