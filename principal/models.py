#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User

class Genre(models.Model):
    title = models.TextField(help_text='Redacta el genero')
    
class Anime(models.Model):
    titulo = models.CharField(max_length=100, unique=True)
    genre = models.ForeignKey(Genre,on_delete=models.CASCADE)
    formato = models.TextField(max_length=100)
    episodios = models.IntegerField()
    
    def __str__(self):
        return self.titulo

class Puntuacion(models.Model):
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime,on_delete=models.CASCADE)
    punt = models.IntegerField()
    
    def __str__(self):
        return self.texto