from django.contrib import admin
from django.urls import path
from group.views import (
    GroupNoticeAPIView, group_list, GroupNoticeDeleteAPIView, GroupCalendarAPIView
)


urlpatterns = [
    path('<int:pk>', GroupNoticeAPIView.as_view(), name="groupDetail"),
    path('calendar/<int:pk>', GroupCalendarAPIView.as_view(), name="groupCalendar"),
    path('<int:id>/notice/<int:pk>', GroupNoticeDeleteAPIView.as_view(), name="groupNoticeDelete"),
    path('', group_list, name="groupList"),
]