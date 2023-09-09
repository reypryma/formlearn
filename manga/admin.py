from django.contrib import admin

from manga.models import Manga, Volume, Genre, SubGenre

# Register your models here.
admin.site.register(Manga)
admin.site.register(Volume)
admin.site.register(Genre)
admin.site.register(SubGenre)