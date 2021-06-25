from django.contrib import admin
from django.urls import path
from feed.views import *

app_name = 'feed'

urlpatterns = [
    path('home/', post_home, name="post_home"),
    path('create/', post_create, name="post_create"),
    path('update/<int:pk>', post_update, name="post_update"),
    path('delete/<int:pk>', post_delete, name="post_delete"),
    path('', feedhome, name="feed_list"),
    path('detail/<int:pk>', post_detail, name="post_detail"),
]

