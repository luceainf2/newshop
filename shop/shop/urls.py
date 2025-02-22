from itertools import product

from django.urls import path
from core.views import main
from playlist.views import playlist, video_like
from playlist.views import video_create
from shop.views import *

urlpatterns = [
    path('playlist/', playlist, name='playlist'),
    path('video_create/', video_create, name='video_create'),
    path('video_like/', video_like, name='video_like'),
    path('', catalog, name='catalog'),
    path('order/', orders, name='order'),
    path('shop/product/<int:product_id>/', product_detail, name='product_detail'),
     path('order_create/<int:product_id>',order_create, name='order_create'),
]

