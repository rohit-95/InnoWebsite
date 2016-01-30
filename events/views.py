from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Events
from .forms import *
#from .forms import Register_Event_Form
from login.models import InnoUser
from django.conf import settings
from django.template import loader
from teams.models import Teams

# Create your views here.

def view_event(request, event_id= None):
	Event = get_object_or_404(Events, id = event_id)
	return render(request, 'events/view_event.html', { 'event' : Event})
	
def edit_event(request, e_id):
	if (request.method == 'GET'):
		form=EditEvent()
		return render(request, 'edit_event.html', {'form': form})

	if(request.method == 'POST'):
		form=EditEvent(request.POST)
		if form.is_valid():
			e = Events.objects.get(event_id = e_id)
			e.event_name = form.cleaned_data['event_name']
			e.details = form.cleaned_data['details']
			e.fb_link = form.cleaned_data['fb_link']
			# Change photo input
    		e.photo = form.cleaned_data['photo']
			e.is_team_event = form.cleaned_data['is_team_event']
			e.min_participants = form.cleaned_data['min_participants']
			e.save()
		return


