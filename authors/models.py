# authors/models.py
from django.core.validators import RegexValidator
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

    def calc_digit(digits):
        s = sum(int(digit) * ((len(digits) + 1 - idx) % 10 + 1) for idx, digit in enumerate(digits))
        return (s * 10) % 11 % 10

    if calc_digit(cpf[:9]) != int(cpf[9]) or calc_digit(cpf[:10]) != int(cpf[10]):
        raise ValidationError(
            _('CPF inválido'),
            code='invalid_cpf',
        )

class Author(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, validators=[RegexValidator(regex=r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', message="CPF deve estar no formato xxx.xxx.xxx-xx")])
    data_nascimento = models.DateField()

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"
