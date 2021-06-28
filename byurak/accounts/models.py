from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from accounts.managers import UserManager


class UserType:
    """
    UserType
    - 서비스제공자와 이용자 구분
    """
    SERVICE_PROVIDER = 'service_provider'
    SERVICE_BUYER = 'service_buyer'

    USER_TYPES = [
        (SERVICE_PROVIDER, '서비스 제공자'),
        (SERVICE_BUYER, '서비스 이용자'),
    ]


class StatusType:
    """
    StatusTYpe
    - 서비스제공자의 경우 관리자 승인을 받아야 함
    - 그로 인해 승인 대기중인 상황 발생
    """
    AVAILABLE = 'available'
    WATING_APPROVAL = 'wating_approval'

    STATUS_TYPES = [
        (AVAILABLE, '사용 가능'),
        (WATING_APPROVAL, '승인 대기'),
    ]



class User(AbstractBaseUser):
    name = models.CharField(max_length=20, null=True, blank=True)
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


class Profile(models.Model):
    EMAIL = 'email'
    KAKAO = 'kakao'
    NAVER = 'naver'
    FACEBOOK = 'facebook'
    INSTAGRAM = 'instagram'

    SIGNUP_TYPES = [
        (EMAIL, 'EMAIL'),
        (KAKAO, 'KAKAO'),
        (NAVER, 'NAVER'),
        (FACEBOOK, 'FACEBOOK'),
        (INSTAGRAM, 'INSTAGRAM')
    ]

    SERVICE_PROVIDER = 'service_provider'
    DEFAULT_USER = 'default_user'

    USER_TYPES = [
        (SERVICE_PROVIDER, 'SERVICE_PROVIDER'),
        (DEFAULT_USER, DEFAULT_USER)
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, help_text='유저')
    user_type = models.CharField(max_length=20, choices=USER_TYPES, default=DEFAULT_USER, help_text='유저 타입')
    signup_type = models.CharField(max_length=10, choices=SIGNUP_TYPES, default=EMAIL, help_text='회원가입 방식')
    address = models.CharField(max_length=127, null=True, blank=True)
    short_introduce = models.CharField(max_length=511, null=True, blank=True)
    image = models.ImageField(upload_to='profile/', blank=True, null=True)
    device_token = models.CharField(max_length=512, null=True, blank=True, help_text='notification 기기 고유 토크값')
    is_push = models.BooleanField(default=True, help_text='notification 수신 여부')
    popularity_score = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.user.name

    @property
    def nickname(self):
        return self.user.nickname

    @property
    def is_signup_finished(self):
        return self.user.is_signup_finish


class ProfileIntroduce(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, help_text='유저 프로필')
    image = models.ImageField(upload_to='profile/profile_introduce', blank=True, null=True)
    description = models.CharField(max_length=511, null=True, blank=True)     

    def __str__(self):
        return self.profile.user.name

    @property
    def user_type(self):
        return self.profile.user_type 
        

class UserFollow(models.Model):
    user_from = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follow_from_set')
    user_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follow_to_set')
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.user_from} follow {self.user_to}'


User.add_to_class('following',
                  models.ManyToManyField('self', through=UserFollow, related_name='followed', symmetrical=False))