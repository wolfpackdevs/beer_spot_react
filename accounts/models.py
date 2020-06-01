from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Brewer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='brewer')
    brewery_name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='brewer/logos/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return f'{self.brewery_name}'

    def __repr__(self):
        return f'{self.brewery_name}'


class BaseUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_use = models.BooleanField(default=True)
    picture = models.ImageField(upload_to='BaseUser/pictures/%Y/%m/%d', null=True,
                                blank=True)

    def __repr__(self):
        return f'{self.user}'

    def __str__(self):
        return f'{self.user}'
        