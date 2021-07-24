from django.contrib import admin
from app_employment.models import *
# Register your models here.


class VacancyAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


admin.site.register(Vacancy, VacancyAdmin)
