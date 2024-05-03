from django.urls import path
from . import views



urlpatterns = [
    path('register/',views.AccountsRegisteView.as_view(), name = "AccountsRegisteView_URL" ),
]
