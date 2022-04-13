from django.contrib import admin

# Register your models here.
from django.forms import forms

from blog3.models import RegisterForm

admin.site.register(RegisterForm)

