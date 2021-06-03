from django.contrib import admin
from django.urls import path
from group.views import group_detail, group_list


urlpatterns = [
    path('<int:pk>', group_detail, name="groupDetail"),
    path('', group_list, name="groupList"),
]