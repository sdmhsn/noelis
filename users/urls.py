from django.urls import path

from . import views

urlpatterns = [
    path('', views.users, name='users'),
    path('author/<str:pk>/', views.author, name='author'),

    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),

    path('account/', views.userAccount, name='account'),
    path('edit-account/', views.editAccount, name='edit-account'),
]
