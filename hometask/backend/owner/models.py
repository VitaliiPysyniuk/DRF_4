from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from .managers import OwnerManager


class OwnerModel(AbstractBaseUser, PermissionsMixin):
    class Meta:
        db_table = 'owners'

    username = None
    is_staff = None
    is_active = None
    last_login = None

    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=20)
    capital = models.IntegerField()
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = OwnerManager()
