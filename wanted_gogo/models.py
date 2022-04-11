from operator import mod
from statistics import mode
from django.db import models


class Funding(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    author = models.CharField(max_length=100)
    target_price = models.IntegerField(null=True)
    session_price = models.IntegerField(null=True)
    end_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.title