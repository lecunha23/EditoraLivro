
import re
from django import forms
from .models import Author


class AuthorForm(forms.ModelForm):
    ...

    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']

        # Implemente aqui a validação do CPF usando expressão regular
        cpf_pattern = re.compile(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$')
        if not cpf_pattern.match(cpf):
            raise forms.ValidationError('CPF deve estar no formato xxx.xxx.xxx-xx')

        return cpf

    class Meta:
        model = Author
        fields = ['nome', 'sobrenome', 'data_nascimento', 'cpf']
