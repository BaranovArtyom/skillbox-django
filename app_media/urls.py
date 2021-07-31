from django.urls import path
from .import views
import os

urlpatterns = [
    path('upload_file/', views.UploadFileView.as_view(), name='upload_file')

]