from django.db import models

class Buyer(models.Model):
    objects = None
    name = models.CharField(max_length=70)
    balance = models.DecimalField(max_digits=100000, decimal_places=2)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Game(models.Model):
    objects = None
    title = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10000, decimal_places=2)
    size = models.DecimalField(max_digits=100000, decimal_places=3)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='buyers')