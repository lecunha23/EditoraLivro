from django.shortcuts import render, get_object_or_404, redirect
from .models import Fornecedor
from .forms import FornecedorForm
import logging

logger = logging.getLogger(__name__)

def lista_fornecedores(request):
    fornecedores = Fornecedor.objects.all()
    return render(request, 'fornecedores/lista_fornecedores.html', {'fornecedores': fornecedores})

def adicionar_fornecedor(request):
    if request.method == 'POST':
        form = FornecedorForm(request.POST)
        if form.is_valid():
            fornecedor = form.save()
            logger.debug("Fornecedor salvo com sucesso")
            return redirect('detalhe_fornecedor', pk=fornecedor.pk)
        else:
            logger.debug("Formulário inválido: %s", form.errors)
            print("Formulário inválido:", form.errors)
    else:
        form = FornecedorForm()
    return render(request, 'fornecedores/adicionar_fornecedor.html', {'form': form})

def editar_fornecedor(request, pk):
    fornecedor = get_object_or_404(Fornecedor, pk=pk)
    if request.method == 'POST':
        form = FornecedorForm(request.POST, instance=fornecedor)
        if form.is_valid():
            form.save()
            return redirect('detalhe_fornecedor', pk=fornecedor.pk)
        else:
            print("Formulário inválido:", form.errors)
    else:
        form = FornecedorForm(instance=fornecedor)
    return render(request, 'fornecedores/editar_fornecedor.html', {'form': form})

def deletar_fornecedor(request, pk):
    fornecedor = get_object_or_404(Fornecedor, pk=pk)
    if request.method == 'POST':
        fornecedor.delete()
        return redirect('lista_fornecedores')
    return render(request, 'fornecedores/deletar_fornecedor.html', {'fornecedor': fornecedor})

def detalhe_fornecedor(request, pk):
    fornecedor = get_object_or_404(Fornecedor, pk=pk)
    return render(request, 'fornecedores/detalhe_fornecedor.html', {'fornecedor': fornecedor})

def index(request):
    return render(request, 'fornecedores/index.html')
