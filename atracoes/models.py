from django.db import models

# Create your models here.
class Atracao(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    schedule = models.TextField()
    min_age = models.IntegerField()

    def __str__(self):
        return self.name