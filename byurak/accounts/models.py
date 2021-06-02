from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from accounts.managers import UserManager


class AddressCategory:
    """
    AddressCategory
    - for user signup, need Refactoring
    - please add region 
    """
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


class InterestCategory:
    COMPUTER = 'Computer'
    ENGLISH = 'English'
    UNIVERSITY_ENTRANCE = 'University_entrance'
    CERTIFICATE = 'Certificate'
    FOREIGN_LANGUAGE = 'Foreign_language'
    DESIGN = 'Design'
    INTERVIEW = 'Interview'
    ETC = 'Etc'
    NONE = 'None'

    INTEREST_TYPES = [
        (COMPUTER, '컴퓨터'),
        (ENGLISH, '영어'),
        (UNIVERSITY_ENTRANCE, '대입'),
        (CERTIFICATE, '자격증'),
        (FOREIGN_LANGUAGE, '외국어'),
        (DESIGN, '디자인'),
        (INTERVIEW, '면접'),
        (ETC, '기타'),
        (NONE, '없음')
    ]



class User(AbstractBaseUser):
    name = models.CharField(max_length=10, null=True, blank=True)
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )
    region_type = models.CharField(max_length=30, choices=AddressCategory.REGION_TYPES, default=AddressCategory.FIRST_REGION, help_text='지역 등록')
    interest_type1 = models.CharField(max_length=30, choices=InterestCategory.INTEREST_TYPES, default=InterestCategory.NONE)
    interest_type2 = models.CharField(max_length=30, choices=InterestCategory.INTEREST_TYPES, default=InterestCategory.NONE)
    interest_type3 = models.CharField(max_length=30, choices=InterestCategory.INTEREST_TYPES, default=InterestCategory.NONE)
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

    user = models.OneToOneField(User, on_delete=models.CASCADE, help_text='유저')
    signup_type = models.CharField(max_length=10, choices=SIGNUP_TYPES, default=EMAIL, help_text='회원가입 방식')
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