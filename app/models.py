from django.db import models
from django.contrib.auth.models import User

class Carros(models.Model):
    modelo = models.CharField(max_length=150)
    marca = models.CharField(max_length=100)
    ano = models.IntegerField()

class Produtos(models.Model):
    Pessoa = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    image = models.CharField(max_length=100)
    price = models.CharField(max_length=100)

class venda(models.Model):
    total = models.FloatField()

class Pedidos(models.Model):
    Pessoa = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.CharField(max_length=100, null=True, blank=True)
    valor = models.IntegerField(null=True)
    quantidade = models.CharField(max_length=100, null=True, blank=True)


class itens_vendido(models.Model):
    Pessoa = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.CharField(max_length=100, null=True, blank=True)
    valor = models.IntegerField(null=True)
    quantidade = models.CharField(max_length=100, null=True, blank=True)
    venda_id = models.IntegerField(null=True)



class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Contato(models.Model):
    nome = models.CharField(max_length=150)
    sobrenome = models.CharField(max_length=255, blank=True)
    telefone = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True)
    descricao = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    mostrar = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

