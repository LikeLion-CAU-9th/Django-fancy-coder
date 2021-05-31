from django.utils.translation import ugettext as _
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(
        self,
        name,
        email,
        phone_number,
        nickname,
        region_type,
        birth_day,
        password=None
    ):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            name=name,
            email=self.normalize_email(email),
            phone_number=phone_number,
            nickname=nickname,
            region_type=region_type,
            birth_day=birth_day,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone_number, nickname, password):
        user = self.create_user(
            email,
            password=password,
            nickname=nickname,
            phone_number=phone_number,
            # phoneNumber = phoneNumber,

        )
        user.is_admin = True
        is_signup_finish = True
        is_signup_first_step = True
        is_login = True
        
        user.save(using=self._db)
        return user
