from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Events
#from .forms import Register_Event_Form
from login.models import InnoUser
from django.conf import settings
from django.template import loader
from teams.models import Teams

# Create your views here.

def view_event(request, event_id= None):
	Event = get_object_or_404(Events, id = event_id)
	return render(request, 'events/view_event.html', { 'event' : Event})
	
	

