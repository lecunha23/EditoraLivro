from django.test import TestCase
from django.urls import reverse
from .models import Livro

class LivroCreateViewTests(TestCase):

    def test_livro_create_view_get(self):
        """
        Testa a exibição do formulário de criação de livros.
        """
        url = reverse('livro_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/form.html')

    def test_livro_create_view_post(self):
        """
        Testa a criação de um novo livro.
        """
        url = reverse('livro_create')
        data = {
            'titulo': 'O Senhor dos Anéis',
            'autor': 'J.R.R. Tolkien',
            'isbn': '978-3-16-148410-0',
            'data_publicacao': '1954-07-29',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)  # Redirecionamento após criação
        self.assertTrue(Livro.objects.filter(titulo='O Senhor dos Anéis').exists())
