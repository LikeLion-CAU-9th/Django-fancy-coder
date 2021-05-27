from django.contrib import admin
from django.urls import path
from feed.views import service_landing


urlpatterns = [
    path('', service_landing, name="landing"),
]

