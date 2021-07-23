from django.urls import path
from .import views
import os

urlpatterns = [
    path('register/', views.UserFormView.as_view(), name='register'),
    path('<int:profile_id>/edit/', views.UserEditFormView.as_view(), name='edit'),

]