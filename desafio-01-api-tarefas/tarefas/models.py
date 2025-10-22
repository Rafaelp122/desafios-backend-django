from django.db import models


class Tarefa(models.Model):
    titulo = models.CharField()
    descricao = models.TextField()
    concluida = models.BooleanField(default=False)
