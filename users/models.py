from django.contrib.auth.models import AbstractUser
from django.db import models

from constants import NULLABLE


class User(AbstractUser):
    username = models.CharField(max_length=155, verbose_name='username')
    email = models.EmailField(max_length=255, unique=True, verbose_name='email')
    phone = models.CharField(max_length=50, **NULLABLE, verbose_name='phone')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

