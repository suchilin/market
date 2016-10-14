# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Unit(models.Model):
    name = models.CharField(max_length=30, unique=True)
    symbol = models.CharField(max_lenght=5)
    description = models.TextField()

class Feature(models.Model):
    name = models.CharField(max_length=30)
    quantity = models.FloatField()
    units = models.OneToOneField(Units, related_name='unit_of')
    description = models.TextField()

class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    features = models.ManyToManyField(Feature, related_name='features')
