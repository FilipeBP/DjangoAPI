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
    comments = models.ManyToManyField(Comment, blank=True)
    reviews = models.ManyToManyField(Review, blank=True)
    localization = models.ForeignKey(Localization, on_delete=models.CASCADE, null=True, blank=True)
    photo = models.ImageField(upload_to='pontos_turisticos', blank=True, null=True)

    def __str__(self):
        return self.name


