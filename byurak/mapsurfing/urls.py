from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('depth2', depth2 , name="depth2"),
    path('depth1', depth1 , name ="depth1"),
]