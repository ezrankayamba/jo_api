from django.urls import path, include
from . import views

urlpatterns = [
    path('jo', views.JoAPI.as_view()),
    path('jo/token', views.JoFetchToken.as_view()),
]
