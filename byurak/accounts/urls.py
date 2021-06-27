from django.contrib import admin
from django.urls import path
import accounts.views


urlpatterns = [
    path('', accounts.views.index, name="index"),
    path('producerProfile', accounts.views.producerProfile, name="producer"),
]

