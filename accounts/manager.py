
# from django.contrib.auth.models import BaseUserManager

# class UserManager(BaseUserManager):
#     use_in_migrations = True

#     def _create_user(self, mobile_number,password, email=None,  **extra_fields):
#         """
#         Create and save a user with the given username, email, and password.
#         """
#         # if not email:
#         #     raise ValueError("The given email must be set")
#         user = self.model(
#             mobile_number=mobile_number,
#             email=self.normalize_email(email),
#             **extra_fields
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_user(self, mobile_number, email=None, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', False)
#         extra_fields.setdefault('is_superuser', False)
#         return self._create_user(mobile_number, email, password, **extra_fields)

#     def create_superuser(self, mobile_number, email=None, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')

#         return self._create_user(mobile_number, email, password, **extra_fields)


from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, mobile_number, password=None, **extra_fields):
        if not mobile_number:
            raise ValueError('The Mobile Number must be set')
        user = self.model(mobile_number=mobile_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, mobile_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(mobile_number, password, **extra_fields)