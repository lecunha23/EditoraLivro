# authors/forms.py

from django import forms
from .models import Author

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['nome', 'sobrenome', 'data_nascimento', 'cpf']
        labels = {
            'nome': 'Nome',
            'sobrenome': 'Sobrenome',
            'data_nascimento': 'Data de Nascimento',
            'cpf': 'CPF',
        }
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
            'cpf': forms.TextInput(attrs={'placeholder': '000.000.000-00'}),
        }
