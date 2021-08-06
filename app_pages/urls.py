from django.urls import path
from .views import *


urlpatterns = [
    path('example', translation_example, name='example')
]