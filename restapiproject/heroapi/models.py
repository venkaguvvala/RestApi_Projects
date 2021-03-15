from django.db import models

# Create your models here.
class Hero(models.Model):
    name=models.CharField(max_length=50)
    alias=models.CharField(max_length=50)

class Heroine(models.Model):
    name=models.CharField(max_length=50)
    alias=models.CharField(max_length=50)
