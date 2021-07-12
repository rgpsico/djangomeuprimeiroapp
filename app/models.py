from django.db import models

class Carros(models.Model):
    modelo = models.CharField(max_length=150)
    marca = models.CharField(max_length=100)
    ano = models.IntegerField()

class Produtos(models.Model):
    name = models.CharField(max_length=150)
    image = models.CharField(max_length=100)
    price = models.CharField(max_length=100)

class venda(models.Model):
    total = models.FloatField()

class Pedidos(models.Model):
    item = models.CharField(max_length=100, null=True, blank=True)
    valor = models.CharField(max_length=100, null=True, blank=True)
    quantidade = models.CharField(max_length=100, null=True, blank=True)
    usuario = models.CharField(max_length=100, null=True, blank=True)



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

