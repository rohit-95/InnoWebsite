from __future__ import unicode_literals

from django.db import models
from login.models import InnoUser


class Events(models.Model):
    name = models.CharField(max_length=30)
    details = models.TextField
    fb_link = models.URLField
    time = models.TimeField
    date = models.DateField
    photo = models.ImageField(upload_to='event_pics/', blank=True)
    min_participants = models.IntegerField(default=1)
    is_team_event = models.BooleanField(default=False)
    participants = models.ManyToManyField(InnoUser, related_name='participating')
    # If is_team_event is true then team captains can be stored
    # in participants and team details can be extracted from there
    # teams = models.ManyToManyField('teams.Teams', related_name='teams')
    managers = models.ManyToManyField(InnoUser, related_name='managing')
    winners = models.ManyToManyField(InnoUser, related_name='winnings')
