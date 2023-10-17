from django.shortcuts import render
from .models import Music  # Importe seu modelo Music aqui

def get_musics(request):
    # Supondo que você queira recuperar todos os objetos Music
    musics = Music.objects.all()  # Isso depende da estrutura do seu modelo Music

    # Crie um contexto com os dados que você deseja passar para o template
    context = {
        'musics': musics,  # Passa os objetos Music para o template
    }

    # Renderize o template 'list.html' com o contexto
    return render(request, 'template.html', context)

def get_music_by_name(request):
    # Supondo que você queira recuperar todos os objetos Music
    musics = Music.music_name  # Isso depende da estrutura do seu modelo Music

    # Crie um contexto com os dados que você deseja passar para o template
    context = {
        'musics': musics,  # Passa os objetos Music para o template
    }

    # Renderize o template 'list.html' com o contexto
    return render(request, 'template.html', context)
