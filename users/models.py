from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    email = models.EmailField( verbose_name='email', max_length=255, unique=True)
    avatar = models.CharField(max_length=500)
    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'


    def get_username(self):
        return self.email


