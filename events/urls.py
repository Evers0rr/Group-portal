from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.event_create, name='event_create'),
    path('edit/<int:pk>/', views.event_edit, name='event_edit'),
    path('delete/<int:pk>/', views.event_delete, name='event_delete'),
    path('calendar/', views.event_calendar, name='event_calendar'),
]
