from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^(\w+)$', views.welcome),
    url(r'liste/', views.liste),
]
