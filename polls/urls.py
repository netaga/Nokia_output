from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index),
    path('device/<int:device_id>', views.device, name='device')
]
