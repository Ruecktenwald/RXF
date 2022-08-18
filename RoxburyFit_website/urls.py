from django.contrib import admin
from django.urls import path, include


from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('RoxburyFit_website.apps.public.urls')),
    path("accounts/", include('RoxburyFit_website.apps.accounts.urls'), name="profile"),

]
