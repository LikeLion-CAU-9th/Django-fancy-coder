from django.db import models
from django.utils import timezone
import datetime
from accounts.models import User

"""
Implementation List
1. Group class
2. Group Community class
3. Group Notice class
4. Pending List class
5. Group Calendar class
6. Group Comment class
"""


class Group(models.Model):

    COMPLETE = 'complete'
    RECRUITMENT = 'recruitment'
    OVERDUE = 'overdue'

    STATUS_TYPES = [
        (COMPLETE, 'COMPLETE'),
        (RECRUITMENT, 'RECRUITMENT'),
        (OVERDUE, 'OVERDUE')
    ]
    title = models.CharField(max_length=30, null=True, blank=True)
    users = models.CharField(max_length=255, null=True, blank=True)
    mento_users = models.CharField(max_length=255, null=True, blank=True)
    mentee_users = models.CharField(max_length=255, null=True, blank=True)
    limited_user_numbers = models.IntegerField(
        default=1, null=True, blank=True)
    status = models.CharField(
        max_length=31, choices=STATUS_TYPES, default=RECRUITMENT, help_text='그룹 상태')
    representive = models.ForeignKey(
        User, on_delete=models.CASCADE, help_text='유저')
    start_date = models.DateTimeField(
        default=timezone.now,
        blank=True,
        null=True,
        verbose_name='그룹 시작일'
    )
    end_date = models.DateTimeField(
        default=timezone.now() + datetime.timedelta(days=1),
        blank=True,
        null=True,
        verbose_name='그룹 마침일'
    )
    keyword = models.CharField(max_length=63, null=True, blank=True)
    short_description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title

    @staticmethod
    def get_splited_users(users):
        return users.split(',')

    @property
    def get_users(self):
        users_information = []
        users = self.get_splited_users(self.users)

        for user_id in users:
            try:
                user = User.objects.get(id=user_id)
            except UserDoesNotExist:
                user = ''
            users_information.append(user)
        return users_information

    @property
    def get_mento_users(self):
        mento_users_information = []
        mento_users = self.get_splited_users(self.mento_users)
        for user_id in mento_users:
            try:
                user = User.objects.get(id=user_id)
            except UserDoesNotExist:
                user = ''
            mento_users_information.append(user)
        return mento_users_information    


class AbstractGroupBaseInfo(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, help_text='그룹')
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text="유저")
    title = models.CharField(max_length=127, null=True, blank=True)
    body = models.TextField(help_text="내용")
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        abstract = True

    @property
    def is_group_representive(self, user):
        if user == self.group.representive:
            return True
        return False


class GroupNotice(AbstractGroupBaseInfo):
    class Meta:
        db_table = 'group_notice'


class GroupCommunityPost(AbstractGroupBaseInfo):
    class Meta:
        db_table = 'group_community_post'


class GroupCalendar(AbstractGroupBaseInfo):
    plan_date = models.DateTimeField()
    class Meta:
        db_table = 'group_calendar'