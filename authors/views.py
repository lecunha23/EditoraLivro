from django.shortcuts import render, get_object_or_404, redirect
from .models import Author
import logging
from django.shortcuts import render, redirect
from .forms import AuthorForm
from django.contrib import messages

logger = logging.getLogger(__name__)

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'authors/author_list.html', {'authors': authors})

def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, 'authors/author_detail.html', {'author': author})

def author_create(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save()
            logger.info(f'Autor criado com sucesso: {author.nome} {author.sobrenome}')
            messages.success(request, 'Autor criado com sucesso.')
            return redirect('author_list')  # Redireciona para a lista de autores após o salvamento
    else:
        form = AuthorForm()
    return render(request, 'authors/author_form.html', {'form': form})

def author_update(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('author_list')
    else:
        form = AuthorForm(instance=author)
    return render(request, 'authors/author_form.html', {'form': form})


def author_delete(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        author.delete()
        return redirect('author_list')
    return render(request, 'authors/author_confirm_delete.html', {'author': author})
