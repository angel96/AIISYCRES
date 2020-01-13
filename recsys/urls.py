"""recetario1 URL Configuration


"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.views import static
from principal import views

urlpatterns = [
    path('', views.index),
    path('populate/', views.populateDB),
    path('loadRS', views.loadRS),
    path('mostValuedAnimes', views.mostValuedAnimes),
    path('similarAnimes', views.similarAnimes),
    path('recommendedUsersAnimes', views.recommendedUsersAnimes),
    path('searchGenero', views.search),
    path('admin/', admin.site.urls),
    ]
