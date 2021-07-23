from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import SelectDateWidget
from django.core.exceptions import ValidationError
from .models import *
import datetime


class AddNewsForm(forms.ModelForm):

    class Meta:
        model = News
        fields = '__all__'


class AddCommentAuthenticForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = '__all__'
        exclude = ['news', 'user', 'user_name']


class AddCommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = '__all__'
        exclude = ['news', 'user']


class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
