from django.contrib import admin
from django.urls import path
from group.views import GroupNoticeAPIView, group_list, GroupNoticeDeleteAPIView


urlpatterns = [
    path('<int:pk>', GroupNoticeAPIView.as_view(), name="groupDetail"),
    path('<int:id>/notice/<int:pk>', GroupNoticeDeleteAPIView.as_view(), name="groupNoticeDelete"),
    path('', group_list, name="groupList"),
]