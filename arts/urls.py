from . import views
from django.urls import path

urlpatterns = [
    path('galery/user:<int:owner_id>' , views.view_photo, name = 'galery'),
    path('galery/add' , views.add_photo, name = 'galeryAdd'),
    path('galery/user:<int:owner>/delete',views.delete_photo, name = 'galertDelete'),
]