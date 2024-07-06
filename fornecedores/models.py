

from django.db import models

class Fornecedor(models.Model):
    nome = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18, unique=True)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    endereco = models.TextField()
    bairro = models.CharField(max_length=255, blank=True, null=True)
    cep = models.CharField(max_length=10, blank=True, null=True)
    cidade = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nome