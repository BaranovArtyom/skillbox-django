from django.urls import path
from .import views
import os

urlpatterns = [
    path('', views.NewsListView.as_view(), name='news'),
    path('add-news/', views.AddNewsFormView.as_view(), name='add_news'),
    path('<int:pk>/', views.NewsDetailView.as_view(), name='detail_news'),
    path('<int:news_id>/edit/', views.EditNewsFormView.as_view(), name='edit_news'),
    path('<int:news_id>/edit/add-comment/', views.EditNewsFormView.as_view(), name='add_comment'),

]