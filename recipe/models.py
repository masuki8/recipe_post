from django.db import models

class Recipe(models.Model):
    title = models.CharField()
    content = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)