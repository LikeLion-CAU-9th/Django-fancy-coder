from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from accounts.managers import UserManager


class AddressInformation:
    FIRST_REGION = 'first_region'
    SECOND_REGION = 'second_region'
    THIRD_REGION =  'third_region'
    FOURTH_REGION = 'fourth_region'
    FIFTH_REGION = 'fifth_region'
    SIXTH_REGION = 'sixth_region'
    SEVENTH_REGION = 'seventh_region'
    EIGHTH_REGION = 'eighth_region'

    REGION_TYPES = [
        (FIRST_REGION, '성동구, 광진구, 성북구'),
        (SECOND_REGION, '서초구, 강남구'),
        (THIRD_REGION, '용산구, 중구, 종로구'),
        (FOURTH_REGION, '여의도구, 영등포구'),
        (FIFTH_REGION, '도봉구, 강북구, 노원구'),
        (SIXTH_REGION, '양천구, 강서구, 구로구, 영등포구'),
        (SEVENTH_REGION, '서대문구, 은평구'),
        (EIGHTH_REGION, '관악구, 금천구, 동장구'),
    ]


class User(AbstractBaseUser):


    name = models.CharField(max_length=10, null=True, blank=True)
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )
    region_type = models.CharField(max_length=30, choices=AddressInformation.REGION_TYPES, default=AddressInformation.FIRST_REGION, help_text='지역 등록')
    nickname = models.CharField(max_length=8, blank=True, null=True, unique=True)
    phone _number = models.CharField(max_length=14, null=True, unique=True)
    withdrew_at = models.DateTimeField(blank=True, null=True, verbose_name='탈퇴 시점')
    birth_day = models.CharField(max_length=32, blank=True, help_text='생년월일')
    is_login = models.BooleanField(default=False)
    is_signup_first_step = models.BooleanField(default=False)
    is_signup_finish = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname', 'phone_number']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin