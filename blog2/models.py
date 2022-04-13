from django.db import models

# Create your models here.
from django.db.models import CASCADE


class Book(models.Model):
    image = models.ImageField(upload_to='Model_images')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Comment(models.Model):
    name = models.CharField(max_length=50)
    comment = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class Video(models.Model):
    menu = models.ForeignKey(Menu, on_delete=CASCADE, blank=True)
    name = models.CharField(max_length=100, blank=True)
    video = models.FileField(upload_to='Model_videos', blank=True)

    def __str__(self):
        return self.name


class Menu_part(models.Model):
    menu_name = models.ForeignKey(Menu, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class Menu_date(models.Model):
    menu_part_name = models.ForeignKey(Menu_part, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=200, blank=True)
    main = models.CharField(max_length=600, blank=True)

    def __str__(self):
        return self.name
