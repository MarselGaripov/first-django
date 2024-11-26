from django.contrib import admin
from django.urls import path, include
from .view import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('post/', post_detail, name='post_detail'),
    path('reviews/', include ('reviews.urls')),
    path('admin/', admin.site.urls),
]
