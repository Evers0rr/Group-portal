from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from events import views as events_views

urlpatterns = [
    path('', events_views.home, name='home'),  # головна сторінка з подіями
    path('admin/', admin.site.urls),
    path('events/', include('events.urls')),
    path('surveys/', include('surveys.urls')),
    path('polls/', include('polls.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/accounts/login/'), name='logout'),
]
