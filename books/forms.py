from django import forms
from .models import Livro
from .validators import validar_isbn


class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'isbn', 'data_publicacao',]
        widgets = {
            'isbn': forms.TextInput(
                attrs={'pattern': '[0-9Xx]*', 'title': 'Digite apenas números e, se necessário, "X" para ISBN-10'}),
            'data_publicacao': forms.DateInput(attrs={'type': 'date'}),  # Adicionar o seletor de data
        }

    def clean_isbn(self):
        isbn = self.cleaned_data.get('isbn')
        if not re.match(r'^[0-9Xx]*$', isbn):
            raise forms.ValidationError('ISBN deve conter apenas números e "X" para ISBN-10.')
        return isbn