from django.urls import path
from .import views
import os

urlpatterns = [
    path('vacancy/', views.vacancy_list, name='vacancies'),


]