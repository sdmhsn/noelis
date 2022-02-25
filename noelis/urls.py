from unicodedata import name
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from . import views

from django.contrib.auth import views as auth_views

from .forms import UserPasswordResetForm, UserSetPasswordForm


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('articles/', include('articles.urls')),
    path('users/', include('users.urls')),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='reset-password.html', form_class=UserPasswordResetForm), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='reset-password-sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='reset.html', form_class=UserSetPasswordForm), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='reset-password-complete.html'), name='password_reset_complete'),
    path('tinymce/', include('tinymce.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
