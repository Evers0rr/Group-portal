from . import views
from django.urls import path

urlpatterns = [
    path('galery/user:<int:owner_id>' , views.view_photo, name = 'galery'),
    path('galery/add' , views.add_photo, name = 'galeryAdd'),
    path('galery/user:<int:photo_id>/delete',views.delete_photo, name = 'galertDelete'),
    path('galery/lista/admin' , views.view_photos, name = 'adminCheakGalery'),
    path('galery/list/photo:<int:photo_id>/accept' , views.admin_photo_accept, name = 'adminAccept'),
    path('galery/list/photo:<int:photo_id>/delete', views.admin_photo_delete, name='adminDelete')
]