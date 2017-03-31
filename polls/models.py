from __future__ import unicode_literals
from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=100)

class Transaction(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    value = models.CharField(max_length=100)
    category = models.OneToOneField(Category, on_delete=models.CASCADE)

class Account(models.Model):
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    transactions = models.ForeignKey(Transaction, on_delete=models.CASCADE)


