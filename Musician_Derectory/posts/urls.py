from django.urls import path
from .views import (
    MusicianListView, MusicianCreateView, MusicianUpdateView,
    AlbumCreateView, AlbumUpdateView, AlbumDeleteView
)

urlpatterns = [
    path('', MusicianListView.as_view(), name='musician_list'),
    path('musician/add/', MusicianCreateView.as_view(), name='musician_create'),
    path('musician/<int:id>/edit/', MusicianUpdateView.as_view(), name='musician_update'),
    path('album/add/', AlbumCreateView.as_view(), name='album_create'),
    path('album/<int:id>/edit/', AlbumUpdateView.as_view(), name='album_update'),
    path('album/<int:id>/delete/', AlbumDeleteView.as_view(), name='album_delete'),
]
