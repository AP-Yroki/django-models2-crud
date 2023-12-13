from django.db import models

class Phones(models.Model):
    name = models.CharField(max_length=20, verbose_name='Модель телефона')
    info = models.CharField(max_length=20, verbose_name='Характеристики')
    price = models.CharField(max_length=20, verbose_name='Цена')
    author = models.CharField(max_length=20, verbose_name='Производитель')