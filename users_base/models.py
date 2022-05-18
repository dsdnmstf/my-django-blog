from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    bio = models.CharField(blank=True, null=True, max_length=500)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    username = models.EmailField('email address', unique=True)
    REQUIRED_FIELDS= []