from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=50)
    websites = models.URLField(max_length=100)
    foundation = models.PositiveIntegerField()
    