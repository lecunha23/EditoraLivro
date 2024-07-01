from django.db import models

class Author(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=14)  # Adicionando o campo CPF
    def __str__(self):
        return f'{self.nome} {self.sobrenome}'

    class Meta:
        app_label = 'authors'
