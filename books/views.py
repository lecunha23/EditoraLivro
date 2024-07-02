from django.shortcuts import render, redirect
from .forms import LivroForm

def livro_create(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('livro_list')  # Substitua 'livro_list' pela URL correta
    else:
        form = LivroForm()
    return render(request, 'books/livro_form.html', {'form': form})
