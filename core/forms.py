from django import forms
from .models import Category, Genero

class CategoryForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = ['name', 'active']

class GeneroForm(forms.ModelForm):
    
    class Meta:
        model= Genero
        fields =  ['name', 'active']