from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from blog2 import views
from django.urls import path, include
app_name = "blog2"

urlpatterns = [
    path('python/', views.python, name='python'),
    path('book', views.book, name='book'),
    path('video', views.video, name='video'),
    path('comment', views.comment, name='comment'),
    path('search_video', views.search_video, name='search_video'),
    path('search_book', views.search_book, name='search_book'),
    path('Run/', views.run, name='run'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
