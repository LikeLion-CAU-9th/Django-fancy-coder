from django.contrib import admin
from django.urls import path
from group.views import GroupNoticeAPIView, group_list


urlpatterns = [
    path('<int:pk>', GroupNoticeAPIView.as_view(), name="groupDetail"),
    path('', group_list, name="groupList"),
]