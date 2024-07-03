from django.shortcuts import render, redirect
from .forms import LivroForm
from .models import Livro

def livro_create(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('livro_list')  # Substitua 'livro_list' pela URL correta
    else:
        form = LivroForm()
    return render(request, 'books/livro_form.html', {'form': form})

def livro_list(request):
    livros = Livro.objects.all()
    return render(request, 'books/livro_list.html', {'livros': livros})
