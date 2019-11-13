from django.db import models

class Localization(models.Model):
    country = models.CharField(max_length=70)
    state = models.CharField(max_length=70)
    city = models.CharField(max_length=70)
    row1 = models.CharField(max_length=150)
    row2 = models.CharField(max_length=150, null=True, blank=True)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lat = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.row1