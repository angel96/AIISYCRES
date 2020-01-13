from principal.models import Anime, Genre, Puntuacion
from principal.forms import UserForm, AnimeForm
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404,HttpResponse
from django.conf import settings

# CONJUNTO DE VISTAS

def index(request): 
    return render(request,'index.html')

def populateDB(request):
   # populateDatabase() 
    return render(request,'populate.html')

def loadRS(request):
   # loadDict()
    return render(request,'loadRS.html')

# APARTADO A

#APARTADO E
def search(request):
    if request.method=='GET':
        form = AnimeForm(request.GET, request.FILES)
        if form.is_valid():
            animeId = form.cleaned_data['id']
            anime = get_object_or_404(Anime, pk=animeId)
            return render(request,'anime_list.html', {'anime':anime})
    form=AnimeForm()
    return render(request,'search_anime.html', {'form':form })


def mostValuedAnimes(request):
    
    return render(request,'most_valued_animes.html')
def similarAnimes(request):
    
    return render(request,'similar_animes.html')
def recommendedUsersAnimes(request):
    
    return render(request,'recommended_users_animes.html')


