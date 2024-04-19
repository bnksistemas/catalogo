from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import CategoryForm, GeneroForm

# Create your views here.


def home(request):
    return render(request, 'core/home.html')


def alta_category(request):
    
    data = {
        'form': CategoryForm()
    }
    return render(request, 'core/alta_category.html', data)


def genero(request):
    data ={
        'form': GeneroForm()
        }
    if request.method == 'POST':
        # Estoy enviando el formulario
        genero_form = GeneroForm(data=request.POST)
        if genero_form.is_valid():
            try:
                # Está todo OK
                genero_form.save()
                return redirect(reverse('genero')+'?ok')
            except:
                # Ha habido un error y retorno a ERROR
                return redirect(reverse('genero')+'?error')

    
    
    
    return render(request, 'core/genero.html',data)
