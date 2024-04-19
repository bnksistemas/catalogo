from django.urls import path
from .views import home, alta_category, genero
urlpatterns = [
    # PAGINA DE INICIO
    path('',home, name="home"),
    
    # ALTA CATEGORIAS
    path('alta_category/', alta_category, name="alta_category"),
    
    #GENERO DE PELICULAS
    path('genero/', genero, name="genero")
]