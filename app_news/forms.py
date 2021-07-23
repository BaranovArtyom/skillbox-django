from django import forms
from django.forms.widgets import SelectDateWidget
from django.core.exceptions import ValidationError
from .models import *
import datetime


class AddNewsForm(forms.ModelForm):

    class Meta:
        model = News
        fields = '__all__'

class AddCommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = '__all__'
        exclude =['news']
