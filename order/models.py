from django.db import models

from manga.models import Manga


# Create your models here.
class Order(models.Model):
    ordered_manga = models.ManyToManyField(Manga, related_name='orders')
    order_date = models.DateTimeField(auto_now_add=True)
