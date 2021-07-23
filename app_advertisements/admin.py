from django.contrib import admin
from .models import *


class AdvertisementInLine(admin.TabularInline):
    model = Advertisement

@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    pass

@admin.register(AdvertisementStatus)
class AdvertisementStatusAdmin(admin.ModelAdmin):
    pass

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['id', 'name']
    search_fields = ['email']

    inlines = [AdvertisementInLine]

@admin.register(Rubric)
class RubricAdmin(admin.ModelAdmin):
    pass
