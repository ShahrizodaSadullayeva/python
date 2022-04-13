from django.shortcuts import render
from django.contrib.auth.views import login_required
# Create your views here.


def home(request):
    return render(request, 'blog1/index.html')


def course(request):
    return render(request, 'blog1/Course.html')


def about(request):
    return render(request, 'blog1/about.html')


