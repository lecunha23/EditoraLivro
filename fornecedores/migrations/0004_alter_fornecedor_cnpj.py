# Generated by Django 5.0.6 on 2024-07-10 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fornecedores', '0003_fornecedor_detalhes_alter_fornecedor_bairro_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fornecedor',
            name='cnpj',
            field=models.CharField(max_length=14, unique=True),
        ),
    ]
