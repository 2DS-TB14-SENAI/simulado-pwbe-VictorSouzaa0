from django.shortcuts import render
from .models import Livro
from .forms import LivroForm

def listar_livros(request):
    if request.method == "GET":

        LivroForm = Livro.objects.all()
        form = LivroForm()
    