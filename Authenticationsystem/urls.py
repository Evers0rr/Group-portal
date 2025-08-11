from . import views
from django.urls import path

urlpatterns = [
    path('profile/<int:user_id>', views.Profile_action.profile_view, name='portfolio'),
    path("profile_edit/", views.Profile_action.profile_edit, name='profile_edit'),
    path("registration/",views.registration_view,name = 'registration'),
    path("login/",views.login_view,name = 'login'),
    path('logout/',views.logout_view,name = 'logout'),
    path('profile/profiles/', views.Profile_action.profiles, name = 'profiles')
]