from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'feed'

urlpatterns = [
    path('', service_landing, name="landing"),
    path('home', board_home, name="board_home"),
    path('create/', board_create, name="board_create"),
    path('update/<int:pk>', board_update, name="board_update"),
    path('delete/<int:pk>', board_delete, name="board_delete"),
    path('list/', board_list, name="board_list"),
    path('detail/<int:pk>', board_detail, name="board_detail"),
]

