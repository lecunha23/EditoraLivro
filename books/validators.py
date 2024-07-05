import re
from django.core.exceptions import ValidationError


def validar_isbn(isbn):
    """
    Valida um ISBN-10 ou ISBN-13.
    """
    isbn = isbn.replace('-', '').replace(' ', '')  # Remove hifens e espaços
    if len(isbn) == 10:
        return validar_isbn10(isbn)
    elif len(isbn) == 13:
        return validar_isbn13(isbn)
    else:
        raise ValidationError('ISBN deve ter 10 ou 13 dígitos.')


def validar_isbn10(isbn):
    if not re.match(r'^\d{9}[\dX]$', isbn):
        raise ValidationError('Formato de ISBN-10 inválido.')

    total = sum((i + 1) * int(x) if x != 'X' else 10 for i, x in enumerate(isbn))
    if total % 11 != 0:
        raise ValidationError('ISBN-10 inválido.')


def validar_isbn13(isbn):
    if not re.match(r'^\d{13}$', isbn):
        raise ValidationError('Formato de ISBN-13 inválido.')

    total = sum((1 if i % 2 == 0 else 3) * int(x) for i, x in enumerate(isbn))
    if total % 10 != 0:
        raise ValidationError('ISBN-13 inválido.')
