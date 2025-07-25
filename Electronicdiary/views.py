from django.shortcuts import render
from django.http import HttpResponse
from .models import Student, Subjects, Grade
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import GradeForm
from django.contrib import messages
from django.utils.timezone import now



# Create your views here.

class GrandeList(LoginRequiredMixin, ListView):
    model = Grade
    template_name = 'Electronic_Diary/grade_list.html'
    context_object_name = 'grades'

class CreateGrade(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Grade
    form_class = GradeForm
    template_name = 'Electronic_Diary/grade_create.html'
    success_url = reverse_lazy('grade-list')

    def form_valid(self, form):
        messages.success(self.request, 'Оцінка успішно додана!')
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_staff
    
class UpdateGrade(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Grade
    form_class = GradeForm
    template_name = 'Electronic_Diary/grade_update.html'
    success_url = reverse_lazy('grade-list')

    def form_valid(self, form):
        messages.success(self.request, 'Оцінка успішно оновлена!')
        return super().form_valid(form)
    
    def get_initial(self):
        initial = super().get_initial()
        if not self.object.date:
            initial['date'] = now().date()
        return initial

    def test_func(self):
        return self.request.user.is_staff
    
class DeleteGrade(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Grade
    form_class = GradeForm
    template_name = 'Electronic_Diary/grade_confirm_delete.html'
    success_url = reverse_lazy('grade-list')

    def form_valid(self, form):
        messages.success(self.request, 'Оцінка успішно видалена!')
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_staff





