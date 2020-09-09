from django.db import models

# Create your models here.


class Students(models.Model):
    name = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    email = models.CharField(max_length=30)


class Scores(models.Model):
    name = models.CharField(max_length=10)  #CharField 는 무조건 max_Length 그래야 자동으로 DB에서 결정
    math = models.IntegerField()
    english = models.IntegerField()
    science = models.IntegerField()