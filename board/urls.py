"""board URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_advertisements.urls')),
    path('profiles/', include('app_profiles.urls')),
    path('news/', include('app_news.urls')),
    path('users/', include('app_users.urls')),
    path('employment/', include('app_employment.urls')),
    path('media/', include('app_media.urls')),
    path('pages/', include('app_pages.urls')),
    path('api/', include('app_rest.urls')),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)# Для загрузки файлов
