from django.db import models

class Fornecedor(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Peca(models.Model):
    nome = models.CharField(max_length=255)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE, related_name='pecas')

    def __str__(self):
        return self.nome