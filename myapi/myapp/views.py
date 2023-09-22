from django.shortcuts import render
from .models import Music

# Create your views here.


def get_musics(request):
    list_musics = Music.objects.name
    context = {'musics': list_musics}
    return render(request, '/musics', context)

def get_bests_musics(request):
    list_bests_musics = Music.objects.filter(music_rating='10')
    context = {'best_musics': list_bests_musics}
    return render(request, '/musics/best', context)