from django.urls import path, include

from . import settings
from django.conf.urls.static import static
from django.contrib import admin

from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', include('announcements.urls')),
    path('admin/', admin.site.urls),
    path('events/', include('events.urls')),
    path('surveys/', include('surveys.urls')),
    path('polls/', include('polls.urls')),
    path('forum/', include('forum.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('electronicdiary/', include('Electronicdiary.urls')),
    path('portfolio/',include("portfolio.urls")),
    path('' , include('Authenticationsystem.urls')),
    path('', include('arts.urls'))] + static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)


