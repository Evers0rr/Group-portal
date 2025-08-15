from django.urls import path, include
from .views import MaterialListView, MaterialCreateView, MaterialUpdateView, MaterialDeleteView

urlpatterns = [
    path('', MaterialListView.as_view(), name='material-list'),
    path('create/', MaterialCreateView.as_view(), name='material-create'),
    path('<int:pk>/edit/', MaterialUpdateView.as_view(), name='material-edit'),
    path('<int:pk>/delete/', MaterialDeleteView.as_view(), name='material-delete'),
]

