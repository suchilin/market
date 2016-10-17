# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from products.models import Unit, Product

class UnitListView(ListView):
    model = Unit
    template_name = 'unit_list.html'

class UnitCreateView(CreateView):
    model = Unit
    fields = ['name','symbol','description']
    template_name = 'unit_add.html'
    success_url = reverse_lazy('products:list-units')

class UnitUpdateView(UpdateView):
    model = Unit
    fields = ['name','symbol','description']
    template_name = 'unit_update.html'
    success_url = reverse_lazy('products:list-units')

class UnitDeleteView(DeleteView):
    model = Unit
    template_name = 'unit_delete.html'
    success_url = reverse_lazy('products:list-units')

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'

class ProductCreateView(CreateView):
    model = Product
    fields = ['name','brand','serial_number','manufacturer','description','short_description','components']
    template_name = 'product_add.html'
    success_url = reverse_lazy('products:list-products')

class ProductDetailView(DetailView):
    model = Product
    fields = ['name','brand','serial_number','manufacturer','description','short_description','components']
    template_name = 'product_detail.html'
    success_url = reverse_lazy('products:list-products')

class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name','brand','serial_number','manufacturer','description','short_description','components']
    template_name = 'product_update.html'
    success_url = reverse_lazy('products:list-products')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('products:list-products')
