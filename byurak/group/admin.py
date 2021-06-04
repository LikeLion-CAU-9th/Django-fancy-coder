from django.contrib import admin
from group.models import Group, GroupCommunityPost, GroupNotice, GroupCalendar


admin.site.register(Group)
admin.site.register(GroupCommunityPost)
admin.site.register(GroupNotice)
admin.site.register(GroupCalendar)
