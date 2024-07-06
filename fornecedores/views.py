
from django.shortcuts import render, get_object_or_404, redirect
from .forms import FornecedorForm
from .models import Fornecedor

def cadastrar_fornecedor(request):
    if request.method == 'POST':
        form = FornecedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_fornecedores')
    else:
        form = FornecedorForm()
    return render(request, 'fornecedores/form_fornecedor.html', {'form': form})

def lista_fornecedores(request):
    fornecedores = Fornecedor.objects.all()
    return render(request, 'fornecedores/lista_fornecedores.html', {'fornecedores': fornecedores})

def detalhe_fornecedor(request, pk):
    fornecedor = get_object_or_404(Fornecedor, pk=pk)
    return render(request, 'fornecedores/detalhe_fornecedor.html', {'fornecedor': fornecedor})
