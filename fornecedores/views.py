

from django.shortcuts import render, get_object_or_404, redirect
from .models import Fornecedor

def lista_fornecedores(request):
    fornecedores = Fornecedor.objects.all()
    return render(request, 'fornecedores/lista_fornecedores.html', {'fornecedores': fornecedores})

def adicionar_fornecedor(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        cnpj = request.POST['cnpj']
        telefone = request.POST['telefone']
        email = request.POST['email']
        endereco = request.POST['endereco']
        bairro = request.POST['bairro']
        cep = request.POST['cep']
        cidade = request.POST['cidade']
        Fornecedor.objects.create(nome=nome, cnpj=cnpj, telefone=telefone, email=email, endereco=endereco, bairro=bairro, cep=cep, cidade=cidade)
        return redirect('lista_fornecedores')
    return render(request, 'fornecedores/adicionar_fornecedor.html')

def detalhe_fornecedor(request, pk):
    fornecedor = get_object_or_404(Fornecedor, pk=pk)
    return render(request, 'fornecedores/detalhe_fornecedor.html', {'fornecedor': fornecedor})
