from django.urls import path
from . import views

app_name = "myapp"

urlpatterns = [
    path('musics/', views.get_musics, name='list_musics'),

    path('musics/<str:music_name>/', views.get_music_by_name, name='get_music_by_name'),
]