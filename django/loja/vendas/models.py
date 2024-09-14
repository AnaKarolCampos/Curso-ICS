from django.db import models

class Venda(models.Model):
    nome = models.TextField(max_length=50)
    data = models.DateTimeField()
    valor_total = models.DecimalField(decimal_places=2, max_digits=8)
    forma_pagamento = models.CharField(max_length=15)
    observacao = models.TextField(max_length=200)

    def __str__(self):
        return self.nome
    
class Cobranca(models.Model):
    nome_venda = models.TextField(max_length=50)
    valor = models.DecimalField(decimal_places=2, max_digits=8)
    status = models.CharField(max_length=15)
    data_vencimento = models.DateField()
    data_pagamento = models.DateField()
    metodo = models.CharField(max_length=15)

    def __str__(self):
        return self.nome_venda
    
class Entrega(models.Model):
    nome_venda = models.TextField(max_length=50)
    endereco_entrega = models.TextField(max_length=100)
    data_envio = models.DateField()
    data_entrega = models.DateField()
    status = models.CharField(max_length=15)
    codigo_rastreamento = models.CharField(max_length=5)

    def __str__(self):
        return self.nome_venda