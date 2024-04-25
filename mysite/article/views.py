from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import ArticleDB
# Create your views here.



class ArticleListView(ListView):
    model = ArticleDB
    template_name = "article/list.html"
    context_object_name = "articles"


class ArticleDetailView(DetailView):
    model = ArticleDB
    template_name = "article/detail.html"
    context_object_name = "articles"
