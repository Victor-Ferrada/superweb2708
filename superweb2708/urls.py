# Description: URL Configuration for superweb2708 project.
from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name="home"),
    path('faq/', views.faq, name="faq"),
    path('gallery/', views.gallery, name="gallery"),
    path('admin/', admin.site.urls),
]
