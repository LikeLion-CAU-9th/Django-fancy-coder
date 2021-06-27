from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('depth3', depth3 , name="depth3"),
    path('depth1', depth1 , name ="depth1"),
]