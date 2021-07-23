import datetime
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import django.forms.widgets


class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ExtendedRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=20, required=False, help_text='Name')
    last_name = forms.CharField(max_length=20, required=False, help_text='Surname')
    date_of_birth = forms.DateField(required=True, widget=forms.widgets.SelectDateWidget(
                                        years=range(1930, datetime.datetime.now().year + 1)
                                    ),
                                    help_text='Birth date')
    city = forms.CharField(max_length=36, required=False, help_text='City')


    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']
