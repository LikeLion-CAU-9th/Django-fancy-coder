from django.contrib import admin
from group.models import Group, GroupCommunityPost, GroupNotice


admin.site.register(Group)
admin.site.register(GroupCommunityPost)
admin.site.register(GroupNotice)

