from django.urls import path
from .views import GrandeList, CreateGrade, UpdateGrade, DeleteGrade

urlpatterns = [
    path('grades/', GrandeList.as_view(), name='grade-list'),
    path('grades/create/', CreateGrade.as_view(), name='grade-create'),
    path('grades/update/<int:pk>/', UpdateGrade.as_view(), name='grade-update'),
    path('grades/delete/<int:pk>/', DeleteGrade.as_view(), name='grade-delete'),
]