from django.contrib import admin
from . models import Musician, Album

@admin.register(Musician)
class MusicianAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'instrument_type')

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'musician', 'release_date', 'rating')
