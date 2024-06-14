from django.db import models

from . managers import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone


# Create your models here: define our customized user object
class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = None
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=135)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    is_writer = models.BooleanField(default=False, verbose_name="Are you a writer?")

    ## define the unique identifier for authentication as the email, not the username
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    ## define custom user manager class will be the manager for the custom user model
    objects = CustomUserManager()

    def __str__(self):
        return self.email  # when create new object, define the name as email address


