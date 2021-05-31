from django.utils.translation import ugettext as _
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, phone_number, nickname, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            nickname=nickname,
            phone_number=phone_number,
            # phoneNumber = phoneNumber,
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
        user.save(using=self._db)
        return user