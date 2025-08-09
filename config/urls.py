from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from events import views as events_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('announcements.urls')),
    path('admin/', admin.site.urls),
    path('events/', include('events.urls')),
    path('surveys/', include('surveys.urls')),
    path('polls/', include('polls.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/accounts/login/'), name='logout'),
    path('forum/', include('forum.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('electronicdiary/', include('Electronicdiary.urls')),
    path('materials/', include('Materials.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
