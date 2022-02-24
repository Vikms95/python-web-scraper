from os import name
from django.db import models

# Create your models here.

class Actor (models.Model):
    
    name = models.CharField(max_length = 10)
    surname = models.CharField(max_length= 20)
    birthYear = models.IntegerField()
    debutYear = models.IntegerField()

class Film (models.Model):

    name = models.CharField(max_length=30)
    releaseYear = models.IntegerField()


