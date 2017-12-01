from django.db import models

# Create your models here.
class Welcome(models.Model):
    welcomeText = models.CharField(max_length=50)
    lang = models.CharField(max_length=2)
