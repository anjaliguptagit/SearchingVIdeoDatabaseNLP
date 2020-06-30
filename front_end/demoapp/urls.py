from django.urls import path
from . import views

urlpatterns = [
    path('', views.nlp, name='home-page'),
]