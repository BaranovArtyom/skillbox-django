from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView
from .forms import *
from django.views import View
from django.http import HttpResponseRedirect

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
        comment_form = AddCommentForm
        return render(request, 'news/edit.html', context={'news_form': news_form, 'news_id': news_id,
                                                          'comment_form': comment_form})

    def post(self, request, news_id):
        news = News.objects.get(id=news_id)
        news_form = AddNewsForm(request.POST, instance=news)
        comment_form = AddCommentForm(request.POST)

        if comment_form.is_valid():
            Comment.objects.create(**comment_form.cleaned_data)
            comment = Comment.objects.last()
            comment.news = news
            comment.save()

            return HttpResponseRedirect('../')

        if news_form.is_valid():
            news.save()
        return HttpResponseRedirect('../')
