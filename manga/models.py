from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.shortcuts import render


# Create your models here.
class Volume(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Genre(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class SubGenre(models.Model):
    parent_genre = models.OneToOneField(Genre, on_delete=models.CASCADE, blank=True, null=True, unique=True)

    def __str__(self):
        return self.parent_genre.title


class Manga(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='manga_genre', blank=True, null=True)
    sub_genres = models.ManyToManyField(SubGenre, related_name='manga_subgenres', blank=True)
    volume = models.ForeignKey(Volume, on_delete=models.CASCADE, blank=True, null=True)

    def get_available_subgenres(self):
        used_subgenre_ids = self.sub_genres.values_list('id', flat=True)
        available_subgenres = SubGenre.objects.filter(parent_genre=self.genre).exclude(id__in=used_subgenre_ids)
        return available_subgenres

    def save(self, *args, **kwargs):
        if self.genre:
            # Update subgenres based on the selected genre
            self.sub_genres.add(*self.get_available_subgenres())
        super().save(*args, **kwargs)
