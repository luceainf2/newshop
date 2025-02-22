
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core.views import main

from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('shop.urls')),
    path("signup/", views.signup, name="signup"),
    path("signin/", views.signin, name="signin"),
    path('signout/', views.signout, name="signout" ),
    path('profile/',views.profile, name='profile'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)