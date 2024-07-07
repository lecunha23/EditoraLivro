import re
from django import forms
from .models import Livro
from django.forms.widgets import DateInput

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = '__all__'
        widgets = {
            'data_publicacao': DateInput(attrs={'type': 'date'}),  # Configuração para mostrar calendário
        }

    def clean_isbn(self):
        isbn = self.cleaned_data.get('isbn')

        # Remove any hyphens
        isbn = isbn.replace('-', '')

        # Check if ISBN is 10 or 13 characters long
        if len(isbn) not in [10, 13]:
            raise forms.ValidationError('ISBN inválido. Deve ter 10 ou 13 dígitos.')

        # ISBN-10 validation
        if len(isbn) == 10:
            if not re.match(r'^\d{9}[\dX]$', isbn):
                raise forms.ValidationError('ISBN-10 inválido.')
            # Validate ISBN-10 checksum
            total = sum((10 - i) * (10 if x == 'X' else int(x)) for i, x in enumerate(isbn))
            if total % 11 != 0:
                raise forms.ValidationError('ISBN-10 inválido.')

        # ISBN-13 validation
        elif len(isbn) == 13:
            if not re.match(r'^\d{13}$', isbn):
                raise forms.ValidationError('ISBN-13 inválido.')
            # Validate ISBN-13 checksum
            total = sum((1 if i % 2 == 0 else 3) * int(x) for i, x in enumerate(isbn))
            if total % 10 != 0:
                raise forms.ValidationError('ISBN-13 inválido.')

        return self.cleaned_data.get('isbn')
