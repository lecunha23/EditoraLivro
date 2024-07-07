from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
def pagina_inicial(request):
    return render(request, 'pagina_inicial.html')

def lista_fornecedores(request):
    fornecedores = Fornecedor.objects.all()  # Consulta ao modelo Fornecedor
    return render(request, 'fornecedores/lista_fornecedores.html', {'fornecedores': fornecedores})