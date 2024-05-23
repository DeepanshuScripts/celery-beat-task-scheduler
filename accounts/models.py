from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from accounts.manager import UserManager

class UserProfile(AbstractUser):
    mobile_number = PhoneNumberField(_("Mobile Number"),unique=True)
    objects = UserManager()
    USERNAME_FIELD = 'mobile_number'
    # REQUIRED_FIELDS = ['mobile_number']

    def __str__(self):
        return self.mobile_number.as_e164 