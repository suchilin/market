# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Unit(models.Model):
    name = models.CharField(max_length=30, unique=True)
    symbol = models.CharField(max_length=5)
    description = models.TextField()

    def __unicode__(self):
        return self.name

class Feature(models.Model):
    name = models.CharField(max_length=30)
    quantity = models.FloatField()
    units = models.OneToOneField(Unit, related_name='unit_of')
    description = models.TextField()

    def __unicode__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    features = models.ManyToManyField(Feature, related_name='features')
    components = models.ManyToManyField('self', null=True, blank=True)

    def __unicode__(self):
        return self.name
