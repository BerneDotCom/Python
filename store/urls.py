from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^(\w+)$', views.welcome),
    url(r'author/(\w+)$', views.author),
    url(r'author/liste/', views.authorList),
    url(r'articles/liste/', views.articleList),
    url(r'article/(\w+)$', views.article),

]
