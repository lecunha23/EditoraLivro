from django.db import models
from fornecedores.models import Fornecedor

class Peca(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(null=True, blank=True)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return self.nome

