from django.test import TestCase
from django.urls import reverse
from .models import Author

class AuthorCreateViewTests(TestCase):

    def test_author_create_view(self):
        # Testa se a página de criação de autor está acessível
        url = reverse('author_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_author_creation(self):
        # Testa se um autor é criado corretamente no banco de dados
        url = reverse('author_create')
        data = {
            'nome': 'João',
            'sobrenome': 'Silva',
            'data_nascimento': '1990-01-01',
            'cpf': '123.456.789-00',
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)  # Verifica o redirecionamento após o POST
        self.assertTrue(Author.objects.filter(nome='João', sobrenome='Silva').exists())

    def test_author_creation_invalid_data(self):
        # Testa o caso de tentar criar um autor com dados inválidos
        url = reverse('author_create')
        data = {
            'nome': '',  # Nome vazio (deve falhar)
            'sobrenome': 'Silva',
            'data_nascimento': '1990-01-01',
            'cpf': '123.456.789-00',
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)  # Deve retornar status 200 porque o formulário é inválido
        self.assertFalse(Author.objects.filter(nome='', sobrenome='Silva').exists())  # Não deve criar no banco
