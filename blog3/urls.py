from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from blog3 import views
from django.urls import path, include
app_name = "blog3"

urlpatterns = [
    path('registration', views.registration, name='registration'),
    path('signup', views.signup, name='signup'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
