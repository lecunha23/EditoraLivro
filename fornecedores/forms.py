from django import forms
from .models import Fornecedor
from .utils import validar_cnpj

class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['nome', 'cnpj', 'telefone', 'email', 'endereco', 'bairro', 'cep', 'cidade']

    def clean_cnpj(self):
        cnpj = self.cleaned_data.get('cnpj')

        # Verifica se o CNPJ tem exatamente 14 caracteres
        if len(cnpj) != 14:
            raise forms.ValidationError('O CNPJ deve ter exatamente 14 caracteres.')

        # Verifica se o CNPJ contém apenas dígitos (números)
        if not cnpj.isdigit():
            raise forms.ValidationError('O CNPJ deve conter apenas números.')

        # Verifica se o CNPJ é válido usando a função validar_cnpj
        if not validar_cnpj(cnpj):
            raise forms.ValidationError('CNPJ inválido.')

        return cnpj

    def is_valid(self):
        valid = super(FornecedorForm, self).is_valid()
        print("Formulário válido:", valid)
        print("Erros do formulário:", self.errors)
        return valid
