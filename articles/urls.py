from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.articles, name='articles'),
    path('category/<str:categoryInput>/', views.categoryView, name='category'),
    path('article/<str:slugInput>/', views.article, name='article'),
    path('write-article/', views.writeArticle, name='write-article'),
    path('edit-article/<str:pk>', views.editArticle, name='edit-article'),
    path('delete-article/<str:pk>', views.deleteArticle, name='delete-article'),
]
