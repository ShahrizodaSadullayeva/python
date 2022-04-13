from django.contrib import admin
from blog1 import views
from django.urls import path, include
app_name = "blog1"

urlpatterns = [
    path('', views.home, name='home'),
    path('course/', views.course, name='course'),
    path('about', views.about, name='about'),
]


