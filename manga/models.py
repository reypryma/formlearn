from django.db import models
from django.shortcuts import render


# Create your models here.
class Volume(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Manga(models.Model):
    genre = models.CharField(max_length=100)
    sub_genre = models.CharField(max_length=100)
    volume = models.ForeignKey(Volume, on_delete=models.CASCADE)
