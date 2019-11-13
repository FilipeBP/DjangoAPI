from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    mark_choices = [ (0, '0'),
        (1, '1'), (2, '2'),
        (3, '3'), (4, '4'),
        (5, '5'), (6, '6'),
        (7, '7'), (8, '8'),
        (9, '9'), (10, '10')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    mark = models.IntegerField(choices=mark_choices)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name
