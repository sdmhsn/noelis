from django.urls import path
from . import views


urlpatterns = [
    path('', views.articles, name='articles'),
    path('category/<str:cats>/', views.categoryView, name='category'),
    path('article/', views.article, name='article'),
]
