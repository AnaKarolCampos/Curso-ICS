from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField(200)

    def __str__(self):
        return self.nome
    
class Cliente(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField()
    telefone = models.CharField(max_length=11)
    endereco = models.CharField(max_length=150)
    data_nascimento = models.DateField(max_length=10)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome