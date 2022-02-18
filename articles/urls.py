from django.urls import path
from . import views


urlpatterns = [
    path('', views.articles, name='articles'),
    path('<str:cats>/', views.categoryView, name='category'),
    path('article/<str:slugInput>/', views.article, name='article'),
]
