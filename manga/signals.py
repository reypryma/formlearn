from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from manga.models import Genre, SubGenre


@receiver(post_save, sender=Genre)
def create_subgenre(sender, instance, created, **kwargs):
    if created:
        SubGenre.objects.create(parent_genre=instance)


@receiver(post_delete, sender=Genre)
def delete_subgenre(sender, instance, **kwargs):
    try:
        subgenre = SubGenre.objects.get(parent_genre=instance)
        subgenre.delete()
    except SubGenre.DoesNotExist:
        pass


@receiver(post_delete, sender=SubGenre)
def delete_related_genre(sender, instance, **kwargs):
    related_genre = instance.parent_genre
    if related_genre.subgenre_set.count() == 0:
        related_genre.delete()
