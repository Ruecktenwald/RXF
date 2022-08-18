
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),

    #Django Auth
    path('accounts/login', auth_views.LoginView.as_view(template_name="accounts/login.html"), name = 'login'),



]

