# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from products.models import Unit

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
