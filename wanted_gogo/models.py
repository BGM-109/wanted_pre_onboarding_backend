from operator import mod
from statistics import mode
from django.db import models


class Funding(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    author = models.CharField(max_length=100)
    target_price = models.IntegerField
    session_price = models.IntegerField
    end_date = models.DateTimeField

    def __str__(self):
        return self.title