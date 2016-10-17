# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse

# Create your models here.

class Unit(models.Model):
    name = models.CharField(max_length=30, unique=True)
    symbol = models.CharField(max_length=5)
    description = models.TextField()

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products.views.unit', args=[str(self.pk)])

class Product(models.Model):
    name = models.CharField(max_length=30)
    brand = models.CharField(max_length=30, null=True, blank=True)
    serial_number = models.CharField(max_length=30, null=True, blank=True)
    manufacturer = models.CharField(max_length=30, null=True, blank=True)
    description = models.TextField()
    short_description = models.CharField(max_length=255, blank=True)
    components = models.ManyToManyField('self', null=True, blank=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products.views.ProductDetailView', args=[str(self.pk)])

class Feature(models.Model):
    name = models.CharField(max_length=30)
    quantity = models.FloatField()
    units = models.OneToOneField(Unit, related_name='unit_of')
    description = models.TextField()
    product = models.ForeignKey(Product, related_name='features', null=True, blank=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products.views.feature', args=[str(self.pk)])

