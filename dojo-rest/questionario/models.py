from django.db import models

class Questoes(models.Model):
    pergunta = models.CharField(max_length=50, blank=True)
    descricao = models.CharField(max_length=200, blank=True)