from django.contrib import admin

# Register your models here.
from blog2.models import Book, Comment, Video, Menu, Menu_part, Menu_date

admin.site.register(Book)
admin.site.register(Comment)
admin.site.register(Video)
admin.site.register(Menu)
admin.site.register(Menu_part)
admin.site.register(Menu_date)
