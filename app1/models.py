from operator import mod
from pyexpat import model
from statistics import mode
from unicodedata import name
from django.db import models

# Create your models here.
class Company(models.Model):
    cmp_name=models.CharField(max_length=45)
    location=models.CharField(max_length=45)
    def __str__(self):
        return self.cmp_name

class Customer(models.Model):
    name=models.CharField(max_length=45)
    age=models.IntegerField()
    place=models.CharField(max_length=45)
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    def __str__(self):
        return self.name