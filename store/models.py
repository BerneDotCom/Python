from django.db import models

# Create your models here.
class Welcome(models.Model):
    welcomeText = models.CharField(max_length=50)
    lang = models.CharField(max_length=2)

class Author(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)

class Articles(models.Model):
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=150)
    author = models.ForeignKey(Author)
