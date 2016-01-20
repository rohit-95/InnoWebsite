from __future__ import unicode_literals

from django.db import models


class Teams(models.Model):
    name = models.CharField(max_length=50, unique=True)
    members = models.ManyToManyField('login.InnoUser', related_name='member')
    captain = models.OneToOneField('login.InnoUser')