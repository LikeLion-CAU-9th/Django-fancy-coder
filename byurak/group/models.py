from django.db import models
from django.utils import timezone
import datetime

"""
Implementation List
1. Group class
2. Group Community class

"""


class Group(models.Model):
    users = models.JSONField()
    mento_users = models.JSONField()
    mentee_users = models.JSONField()
    representive = models.ForeignKey(User, on_delete=models.CASCADE, help_text='유저')  
    start_date = models.DateTimeField(
        default=timezone.now,
        blank=True,
        null=True,
        verbose_name='그룹 시작일'
    )
    end_date = models.DateTimeField(
        default=timezone.now + datetime.timedelta(days=1),
        blank=True,
        null=True,
        verbose_name='그룹 시작일'
    )
    keyword = models.CharField(max_length=63, null=True, blank=True)
    short_description = models.CharField(max_length=255, null=True, blank=True)
     

class GroupNotice(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, help_text='그룹')
    user = models.Foreignkey(User, on_delete=models.CASCADE, help_text="유저")
    title = models.CharField(max_length=127, null=True, blank=True)
    body = models.TextField(help_text="그룹 공지 글")
    created_at = models.DateTimeField(default=timezone.now)


