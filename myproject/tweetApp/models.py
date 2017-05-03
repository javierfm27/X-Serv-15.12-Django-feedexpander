from django.db import models

# Create your models here.
class User (models.Model):
    nombreUser = models.CharField(max_length=32)
