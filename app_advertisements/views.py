from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from app_advertisements.models import Advertisement


# def advertisement_list(request, *args, **kwargs):
#     advlist = ['Мастер', 'Выведение', 'Услуги', 'Что-то']
#     return render(request, 'advertisement/advertisement_list.html', {'app_advertisements': advlist})

    # return render(request, 'advertisement/advertisement_list.html', {}) # Путь от templates.

    # return HttpResponse('<ul>'
    #                     '<li>Мастер</li>'
    #                     '<li>Выведение</li>'
    #                     '<li>Услуги</li>'
    #                     '<li>Что-то</li>'
    #                     '</ul>')

# def about_us(request, *args, **kwargs):
#     title = 'Something'
#     description = 'Desca dkjffdsrf23 lorem'
#     return render(request, 'advertisement/about.html', {'title': title, 'description': description})

class MainPage(TemplateView):
    template_name = 'advertisement/main_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['regions'] = Regions.regions
        return context

    def post(self, request):
        Advertisements.count += 1
        return HttpResponse('POSTED!')

class Contacts(TemplateView):
    template_name = 'advertisement/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        email = 'sales@company.com'
        phone = '8-800-708-19-45'
        context['email'] = email
        context['phone'] = phone
        return context

# class Advertisements(View):
#     count = 0
#
#     def get(self, request):
#         app_advertisements = Advertisement.objects.all()
#         # advlist = ['Мастер', 'Выведение', 'Услуги', 'Что-то']
#         return render(request, 'advertisement/advertisement_list.html', {
#             'app_advertisements': app_advertisements,
#             'count': Advertisements.count
#         })

    def post(self, requset):
        Advertisements.count += 1
        return HttpResponse('Ok')

class About(TemplateView):
    template_name = 'advertisement/about.html'
    def get_context_data(self, **kwargs):
        title = 'Something'
        description = 'Desca dkjffdsrf23 lorem'
        context = super().get_context_data(**kwargs)
        context['title'] = title
        context['description'] = description
        return context

class Regions(View):
    regions = ['Olalal', 'Hohoho', 'Shetishet', 'kekekEK']
    def get(self, request):
        return render(request, 'advertisement/regions.html', {'regions': Regions.regions})
    def post(self, requset):
        return HttpResponse('Ok')

class AdvertisementListView(ListView):
    model = Advertisement
    template_name = 'advertisement/advertisement_list.html'
    context_object_name = 'advertisement_list'
    queryset = Advertisement.objects.all()[:5]

class AdvertisementDetailView(DetailView):
    model = Advertisement
    template_name = 'advertisement/advertisement_detail.html'
    context_object_name = 'advertisement'



