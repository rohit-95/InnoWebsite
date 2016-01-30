from __future__ import unicode_literals

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class InnoUserManager(BaseUserManager):
    def create_user(self, username, email, dob, gender, first_name, last_name,
                    password=None):
        user = self.model(username=username, email=email, dob=dob,
                          gender=gender, first_name=first_name, last_name=last_name)
        user.set_password(password)
        return user

    def create_superuser(self, username, email, inno_id, dob, gender, first_name, last_name, password):
        user = self.model(username=username, email=email, inno_id=inno_id, dob=dob,
                          gender=gender, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.is_em = True
        user.is_admin = True
        user.save()
        return user


class InnoUser (AbstractBaseUser):
    GENDERS = (
            ('male', 'Male'),
            ('female', 'Female')
        )
    inno_id = models.CharField(max_length=8, unique=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    gender = models.CharField(max_length=20, null=True, blank=True,
                              choices=GENDERS)
    email = models.EmailField(unique=True, db_index=True)
    username = models.CharField(unique=True, max_length=30)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True)
    dob = models.DateField(null=True, blank=True)
    phone_no = models.CharField(max_length=12, default='')
    college = models.CharField(max_length=30)
    course = models.CharField(max_length=30)
    year = models.IntegerField
    date_joined = models.DateTimeField(auto_now_add=True)
    is_em = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = InnoUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['inno_id', 'email']

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
