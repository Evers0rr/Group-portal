from . import views
from django.urls import path


urlpatterns = [
    path('create/',views.Projects.create_project ,name = 'create_project'),
    path('edit/<int:project_id>',views.Projects.edit_project, name = 'edit_project'),
    path('delete/<int:project_id>', views.Projects.delete_project, name = 'delete_project'),
    path("projects/profile/user_id:<int:user_id>", views.Projects.projects, name = 'projects'),
    path("projects/profile/project_id:<int:project_id>", views.Projects.project_view, name = 'project'),
    path("projects/profile/project_id:<int:project_id>/edit", views.Projects.projectMediaAdd, name = 'mediaAdd')
]