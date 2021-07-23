from django import forms
from django.forms.widgets import SelectDateWidget
from django.core.exceptions import ValidationError
from .models import User
import datetime


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = '__all__'



# class UserForm(forms.Form):
#     username = forms.CharField()
#     password = forms.CharField()
#     first_name = forms.CharField()
#     second_name = forms.CharField()
#     last_name = forms.CharField()
#     email = forms.EmailField()
#     birthday = forms.DateField(widget=SelectDateWidget(years=[year for year in range(1970, 2051)]))
#
#     def clean_birthday(self):
#         data = self.cleaned_data['birthday']
#         today = datetime.date.today()
#         delta = (today - data).days / 365
#         if delta < 18:
#             raise ValidationError('Вам меньше 18!')
#         else:
#             return data
#
#     def clean(self):
#         cleaned_data = super(UserForm, self).clean()
#         first_name = cleaned_data.get('first_name')
#         last_name = cleaned_data.get('last_name')
#         if first_name == 'Иван' and last_name == 'Иванов':
#             msg = 'Ты чертов Иван Иванов!'
#             self.add_error('first_name', msg)
#             self.add_error('last_name', msg)
#             # raise ValidationError('Ты чертов Иван Иванов!')








