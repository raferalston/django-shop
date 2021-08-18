from django.db import models

# Create your models here.

class NewsArticle(models.Model):
    article = models.CharField(max_length=100)