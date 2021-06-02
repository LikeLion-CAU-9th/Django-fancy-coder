from django.contrib import admin
from django.urls import path
import group.views


urlpatterns = [
    path('', group.views.group_detail, name="groupDetail"),
]