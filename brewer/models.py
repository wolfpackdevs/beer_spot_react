from django.db import models
from accounts.models import Brewer


class Style(models.Model):
    style = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.style}'

    def __repr__(self):
        return f'{self.style}'


class Flavor(models.Model):
    flavor_note = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return f'{self.flavor_note}'

    def __repr__(self):
        return f'{self.flavor_note}'


class GenericBeer(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='g-beer/images/%Y/%m/%d', null=True, blank=True)
    style = models.ForeignKey(Style, on_delete=models.CASCADE)
    flavor = models.ManyToManyField(Flavor)
    abv = models.FloatField()


class Beer(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='beer/images/%Y/%m/%d', null=True, blank=True)
    brewer = models.ForeignKey(Brewer, on_delete=models.CASCADE)
    style = models.ForeignKey(Style, on_delete=models.CASCADE)
    flavor = models.ManyToManyField(Flavor)
    abv = models.FloatField(blank=True)
    brewer_notes = models.TextField(null=True)
    is_available = models.BooleanField(default=True)
    date_added = models.DateField(auto_now=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name} by {self.brewer}'