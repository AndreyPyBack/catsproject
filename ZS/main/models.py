from django.db import models

class Cats(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    eyes = models.CharField(max_length=100)
    picture = models.ImageField(blank=True, null=True)
    text_cat = models.TextField(blank=True, null=True)
