from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from .models import Livro
from .forms import LivroForm

def livro_create(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('livro_list')
    else:
        form = LivroForm()
    return render(request, 'books/livro_form.html', {'form': form})

def livro_update(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('livro_list')
    else:
        form = LivroForm(instance=livro)
    return render(request, 'books/livro_form.html', {'form': form})

def livro_list(request):
    livros = Livro.objects.all()
    return render(request, 'books/livro_list.html', {'livros': livros})

class LivroDetailView(DetailView):
    model = Livro
    template_name = 'books/livro_detail.html'
    context_object_name = 'livro'




def livro_delete(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        livro.delete()
        return redirect('livro_list')
    return render(request, 'books/livro_confirm_delete.html', {'livro': livro})
