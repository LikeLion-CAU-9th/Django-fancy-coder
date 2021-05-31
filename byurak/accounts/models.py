from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from accounts.managers import UserManager


class User(AbstractBaseUser):
    name = models.CharField(max_length=10, null=True, blank=True)
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )
    nickname = models.CharField(max_length=8, blank=True, null=True, unique=True)
    phone_number = models.CharField(max_length=14, null=True, unique=True)
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