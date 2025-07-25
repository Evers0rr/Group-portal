from django.urls import path
from . import views

urlpatterns = [
    path('', views.survey_list, name='survey_list'),
    path('<int:survey_id>/step/<int:step>/', views.survey_detail, name='survey_detail'),
    path('<int:survey_id>/step/', views.survey_detail, name='survey_detail_first'),
    path('<int:survey_id>/complete/', views.survey_complete, name='survey_complete'),
    path('<int:survey_id>/results/', views.survey_results, name='survey_results'),
]
