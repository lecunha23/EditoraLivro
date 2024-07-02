from django.db import models
from authors.models import Author  # Supondo que o modelo Author esteja no aplicativo authors

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Author, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13)
    data_publicacao = models.DateField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.titulo
