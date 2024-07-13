from django.shortcuts import render, redirect
from .models import Peca
from .forms import PecaForm
from django.shortcuts import get_object_or_404, redirect, render


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

def deletar_peca(request, pk):
    peca = get_object_or_404(Peca, pk=pk)
    if request.method == 'POST':
        peca.delete()
        return redirect('listar_pecas')  # Redirecionar para a página de listagem de peças após a exclusão
    return render(request, 'pecas/deletar_peca.html', {'peca': peca})