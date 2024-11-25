from django.urls import path
from .views import *

urlpatterns = [
    path('', review_list, name='review_list'),
]