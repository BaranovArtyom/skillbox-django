from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView
from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView
from .forms import *
from django.views import View
from django.http import HttpResponseRedirect, HttpResponse


# Create your views here.

class NewsListView(ListView):
    model = News
    template_name = 'news/news_list.html'
    context_object_name = 'news_list'
    queryset = News.objects.order_by('created_at')

class AddNewsFormView(View):
    def get(self, request):
        news_form = AddNewsForm
        return render(request, 'news/add_news.html', context={'news_form': news_form})

    def post(self, request):
        news_form = AddNewsForm(request.POST)

        if news_form.is_valid():
            News.objects.create(**news_form.cleaned_data) # Сохранение в бд.
            return HttpResponseRedirect('/news')
        return render(request, 'news/add_news.html', context={'news_form': news_form})

class NewsDetailView(DetailView):
    model = News
    template_name = 'news/news_detail.html'
    context_object_name = 'news'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = super(NewsDetailView, self).get_object()
        context['comments'] = Comment.objects.filter(news=obj)

        return context

class EditNewsFormView(View):
    def get(self, request, news_id):
        news = News.objects.get(id=news_id)
        news_form = AddNewsForm(instance=news)
        if request.user.is_authenticated:
            comment_form = AddCommentAuthenticForm
        else:
            comment_form = AddCommentForm
        return render(request, 'news/edit.html', context={'news_form': news_form, 'news_id': news_id,
                                                          'comment_form': comment_form})

    def post(self, request, news_id):
        news = News.objects.get(id=news_id)
        news_form = AddNewsForm(request.POST, instance=news)
        if request.user.is_authenticated:
            comment_form = AddCommentAuthenticForm(request.POST)
        else:
            comment_form = AddCommentForm(request.POST)

        if comment_form.is_valid():
            Comment.objects.create(**comment_form.cleaned_data)
            comment = Comment.objects.last()
            comment.news = news
            if isinstance(request.user, User):
                comment.user = request.user
            else:
                user = None
            comment.save()

            return HttpResponseRedirect('../')

        if news_form.is_valid():
            news.save()
        return HttpResponseRedirect('../')


class LoginView(View):
    def get(self, request):
        auth_form = AuthForm
        return render(request, 'news/login.html', context={'form': auth_form})

    def post(self, request):
        auth_form = AuthForm(request.POST)

        if auth_form.is_valid():
            username = auth_form.cleaned_data['username']
            password = auth_form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user:
                if not (datetime.datetime.now().hour in range(22, 25) or
                        datetime.datetime.now().hour in range(0, 9)):
                    if not user.is_superuser:
                        if user.is_active:
                            login(request, user)
                            return HttpResponseRedirect('../')
                        else:
                            auth_form.add_error('__all__', 'User is inactive!')
                    else:
                        auth_form.add_error('__all__', 'User is admin!!')
                else:
                    auth_form.add_error('__all__', 'Go sleep man!')
            else:
                auth_form.add_error('__all__', 'Incorrect user data!')
        return render(request, 'news/login.html', context={'form': auth_form})


class MyLogoutView(LogoutView):
    template_name = 'news/logout.html'
    next_page = '../'
