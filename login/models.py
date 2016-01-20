from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models
from teams.models import Teams


class InnoUser (AbstractUser):
    inno_id = models.CharField(max_length=8, unique=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True)
    dob = models.DateField(null=True, blank=True)
    phone_no = models.CharField(max_length=12, unique=True, default='')
    college = models.CharField(max_length=30)
    course = models.CharField(max_length=30)
    year = models.IntegerField
    is_em = models.BooleanField(default=False)
