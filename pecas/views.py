from django.shortcuts import render, redirect
from .models import Peca
from .forms import PecaForm

def listar_pecas(request):
    pecas = Peca.objects.all()
    return render(request, 'pecas/listar_pecas.html', {'pecas': pecas})

def criar_peca(request):
    if request.method == 'POST':
        form = PecaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_pecas')
    else:
        form = PecaForm()
    return render(request, 'pecas/criar_peca.html', {'form': form})

def editar_peca(request, pk):
    peca = Peca.objects.get(pk=pk)
    if request.method == 'POST':
        form = PecaForm(request.POST, instance=peca)
        if form.is_valid():
            form.save()
            return redirect('listar_pecas')
    else:
        form = PecaForm(instance=peca)
    return render(request, 'pecas/editar_peca.html', {'form': form})
