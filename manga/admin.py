from django.contrib import admin

from manga.models import Manga, Volume

# Register your models here.
admin.site.register(Manga)
admin.site.register(Volume)