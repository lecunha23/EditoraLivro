# authors/models.py

from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re

def validate_cpf(value):
    if not re.match(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', value):
        raise ValidationError(
            _('CPF deve estar no formato "000.000.000-00"'),
            code='invalid_cpf_format',
        )

    cpf = re.sub('[^0-9]', '', value)

    if len(cpf) != 11:
        raise ValidationError(
            _('CPF deve ter 11 dígitos'),
            code='invalid_cpf_length',
        )

    # Validação do dígito verificador do CPF
    cpf = [int(digit) for digit in cpf]
    if (sum(cpf[:9]) * 10 % 11) % 10 != cpf[9] or (sum(cpf[:10]) * 10 % 11) % 10 != cpf[10]:
        raise ValidationError(
            _('CPF inválido'),
            code='invalid_cpf',
        )

class Author(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=14, unique=True, validators=[validate_cpf], verbose_name='CPF')

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'

    class Meta:
        app_label = 'authors'
