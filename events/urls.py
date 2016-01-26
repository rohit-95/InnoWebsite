from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^(?P<event_id>\d+)/$', 'events.views.view_event', name = 'view_event'),
    #url(r'^register/(?P<event_id>\d+)/$', 'events.views.register_event', name = 'register_event'),
]
