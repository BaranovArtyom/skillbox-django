from django.urls import path
from .import views
import os
from rest_framework import routers
from .api import UserViewSet


router = routers.DefaultRouter()
router.register('users', UserViewSet)
urlpatterns = router.urls
