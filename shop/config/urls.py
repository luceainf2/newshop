from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from core.views import main
from playlist.views import playlist, video_like
from playlist.views import video_create
from shop.views import catalog

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='main'),
    path('playlist/', playlist, name='playlist'),
    path('video_create/', video_create, name='video_create'),
    path('video_like/', video_like, name='video_like'),
    path('catalog/', catalog, name='catalog'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
