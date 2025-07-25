from django.urls import path
from . import views

urlpatterns = [
    path('', views.poll_list, name='poll_list'),
    path('create/', views.poll_create, name='poll_create'),
    path('<int:poll_id>/', views.poll_detail, name='poll_detail'),
    path('<int:poll_id>/results/', views.poll_results, name='poll_results'),
    path('<int:poll_id>/edit/', views.poll_edit, name='poll_edit'),
    path('<int:poll_id>/delete/', views.poll_delete, name='poll_delete'),
]
