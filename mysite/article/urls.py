from django.urls import path
from .views import ArticleListView, ArticleDetailView

urlpatterns = [
    path('articles/', ArticleListView.as_view(), name = "articles_ListView_URL" ),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name = "article_DetailView_URL")
]
