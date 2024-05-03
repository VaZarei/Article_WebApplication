from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import ArticleDB
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.views.generic.edit import FormMixin   ###
from .forms import CommentForm
from django.urls import reverse
# Create your views here.

class ArticleListView(ListView):
    model = ArticleDB
    template_name = "article/list.html"
    context_object_name = "articles"

class ArticleDetailView(FormMixin, DetailView):
    model = ArticleDB
    template_name = "article/detail.html"
    context_object_name = "articles"
    form_class = CommentForm


    def get_success_url(self):
        return reverse("article_DetailView_URL", kwargs = {"pk":self.object.id})
        


    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['form'] = CommentForm(initial={"article":self.object, "writer":self.request.user})
        return context
    
    def post(self, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            pass

    def form_valid(self, form):
        form.save()
        return super(ArticleDetailView,self).form_valid(form)
    

    
 
        

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = ArticleDB
    template_name = "article/new.html"
    fields = ['Title', 'Body']

    def form_valid(self, form):
        form.instance.Auther = self.request.user
        return super().form_valid(form)

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ArticleDB
    template_name = "article/edit.html"
    fields = ['Title', 'Body']
    context_object_name = "article"

    def test_func(self):
        obj = self.get_object()
        return obj.Auther == self.request.user

class ArticleDeleteVeiw(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ArticleDB
    template_name = "article/delete.html"
    success_url = reverse_lazy("articles_ListView_URL")
    context_object_name = "articles"

    def test_func(self):
        obj = self.get_object()
        return obj.Auther == self.request.user
    
    
    
    

