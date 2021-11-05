from django.db import models
from django.db.models.deletion import CASCADE


# Create your models here.
class Albums(models.Model):
    title = models.CharField(max_length=100) 
    artist = models.CharField(max_length=100)
    created_at = models.DateField(null=True, blank=True, auto_now_add=True)
