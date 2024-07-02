from django.contrib import admin
from .models import Author
from django.contrib import messages
class AuthorAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        messages.success(request, 'Autor cadastrado com sucesso!')


admin.site.register(Author)
