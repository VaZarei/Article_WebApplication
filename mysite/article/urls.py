from django.urls import path
from .views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteVeiw

urlpatterns = [
    path('articles/', ArticleListView.as_view(), name = "articles_ListView_URL" ),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name = "article_DetailView_URL"),
    path('articles/new/', ArticleCreateView.as_view(), name = "ArticleCreateView_URL"),
    path('article/<int:pk>/edit', ArticleUpdateView.as_view(), name = "ArticleUpdateView_URL" ),
    path('article/<int:pk>/delete', ArticleDeleteVeiw.as_view(), name = "ArticleDeleteView_URL" ),
]
