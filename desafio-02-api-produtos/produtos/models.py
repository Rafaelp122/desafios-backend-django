from django.db import models


class Produto(models.Model):
    nome = models.CharField()
    preco = models.FloatField()
    categoria = models.CharField()
