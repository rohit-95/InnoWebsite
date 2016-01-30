from django import forms
from events.models import *
from login.models import *
from teams.models import *

class EditEvent(forms.Form):
    event_name = forms.CharField(required=True)
    details = forms.TextField(required=True)
    fb_link = forms.URLField
    photo = forms.ImageField(upload_to='event_pics/', blank=True)
    is_team_event = forms.BooleanField(default=False)
    min_participants = forms.IntegerField(default=1)
