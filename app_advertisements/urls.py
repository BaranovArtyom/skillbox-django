from django.urls import path
from .import views
import os

urlpatterns = [
    path('', views.MainPage.as_view(), name='main_page'),
    # path('advertisement-list/', views.Advertisements.as_view(), name='advertisement_list'),
    path('contacts/', views.Contacts.as_view(), name='contacts'),
    path('about/', views.About.as_view(), name='about'),
    path('regions/', views.Regions.as_view(), name='regions'),
    path('advertisements/', views.AdvertisementListView.as_view(), name = 'advertisement'),
    path('advertisements/<int:pk>/', views.AdvertisementDetailView.as_view(), name='advertisement-detail'),

]