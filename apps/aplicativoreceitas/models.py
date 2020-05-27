from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Receita(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nome_receita = models.CharField(max_length=200)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    data_receita = models.DateTimeField(default=datetime.now, blank=True)
    imagem_receita = models.ImageField(upload_to='imagens/%d/%m/%Y/', blank=True)
    modo_edicao = models.BooleanField(default=False)
    def __str__(self):
        return self.nome_receita
