from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    article_title = models.CharField(max_length=200)
    article_text = models.TextField()
    article_date = models.DateTimeField()
    article_cover = models.ImageField(upload_to='images')

    class Meta:
        db_table = 'article'

class Foto(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images')
    foto_article = models.ForeignKey(Article)

    class Meta:
        db_table = 'foto'

class FIO(models.Model):
    name = models.CharField(max_length=50)
    family = models.CharField(max_length=50)
    adress = models.CharField(max_length=200)
    tel = models.CharField(max_length=20)
    email = models.EmailField()
    fio_article = models.ForeignKey(Article)

    class Meta:
        db_table = 'fio'