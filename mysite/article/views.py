from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import ArticleDB
from django.urls import reverse_lazy

# Create your views here.



class ArticleListView(ListView):
    model = ArticleDB
    template_name = "article/list.html"
    context_object_name = "articles"

class ArticleDetailView(DetailView):
    model = ArticleDB
    template_name = "article/detail.html"
    context_object_name = "articles"

class ArticleCreateView(CreateView):
    model = ArticleDB
    template_name = "article/new.html"
    fields = ['Title', 'Body', 'Auther']

class ArticleUpdateView(UpdateView):
    model = ArticleDB
    template_name = "article/edit.html"
    fields = ['Title', 'Body']
    context_object_name = "article"

class ArticleDeleteVeiw(DeleteView):
    model = ArticleDB
    template_name = "article/delete.html"
    success_url = reverse_lazy("articles_ListView_URL")
    context_object_name = "articles"

