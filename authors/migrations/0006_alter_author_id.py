# Generated by Django 5.0.6 on 2024-07-10 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0005_alter_author_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
