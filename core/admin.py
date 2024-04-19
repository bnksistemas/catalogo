from django.contrib import admin
from .models import Category, Genero
admin.site.site_header = 'Administración del Catalogo'
admin.site.index_title = 'Panel de Control'
admin.site.site_title = 'Catalogo Peliculas'

# Register your models here.

# CATEGORÍAS
class CategoryAdmin(admin.ModelAdmin):
	readonly_fields = ('created',)
	list_display = ('name', 'active', 'created')

admin.site.register(Category, CategoryAdmin)

# GENERO
class GeneroAdmin(admin.ModelAdmin):
	readonly_fields = ('created',)
	list_display = ('name', 'active', 'created')

admin.site.register(Genero, GeneroAdmin)
