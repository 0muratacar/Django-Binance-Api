from django.db import models

class Balance(models.Model):
    name = models.CharField(max_length=100)
    balance = models.FloatField()

    def __str__(self):
        return self.name