from django.db import models
from atracoes.models import Atracao
from comentarios.models import Comment
from avaliacoes.models import Review
from localizacao.models import Localization

class TuristicPoint(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    status = models.BooleanField(default=False) #Por padrão, os pontos turísticos devem ser moderados
    atractions = models.ManyToManyField(Atracao)
    comments = models.ManyToManyField(Comment)
    reviews = models.ManyToManyField(Review)
    localization = models.ForeignKey(Localization, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


