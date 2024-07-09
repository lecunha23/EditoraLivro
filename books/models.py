from django.db import models
from authors.models import Author
from .validators import validar_isbn


class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Author, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13, validators=[validar_isbn])
    data_publicacao = models.DateField()
    def __str__(self):
        return self.titulo
