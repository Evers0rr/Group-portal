from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Material
from .forms import MaterialForm

# Create your views here.

class MaterialListView(LoginRequiredMixin, ListView):
    model = Material
    template_name = 'materials/material_list.html'
    context_object_name = 'materials'

class MaterialCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Material
    form_class = MaterialForm
    template_name = 'materials/material_create.html'
    success_url = reverse_lazy('material-list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser

class MaterialUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Material
    form_class = MaterialForm
    template_name = 'materials/material_update.html'
    success_url = reverse_lazy('material-list')

    def form_valid(self, form):
        return super().form_valid(form)
    
    def test_func(self):
        material = self.get_object()
        return self.request.user == material.created_by or self.request.user.is_staff or self.request.user.is_superuser

class MaterialDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Material
    template_name = 'materials/material_confirm_delete.html'
    success_url = reverse_lazy('material-list')

    def test_func(self):
        material = self.get_object()
        return self.request.user == material.created_by or self.request.user.is_staff or self.request.user.is_superuser
    

    

