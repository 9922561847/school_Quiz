from django.db import models

# Create your models here.
class Exam(models.Model):
    question = models.CharField(max_length=100)
    A = models.CharField(max_length=100)
    B = models.CharField(max_length=100)
    C = models.CharField(max_length=100)
    D = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)

