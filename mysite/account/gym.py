# _*_ coding: utf-8 _*_
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django import forms
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime, timedelta
from django.contrib.auth.hashers import make_password
from django.template.loader import get_template
from django import template
from django.contrib.sites.models import Site
from django.utils.http import urlquote_plus
import json

import os
from apiclient.discovery import build
from httplib2 import Http
import oauth2client
from oauth2client import client
from oauth2client import tools

from account.models import *
from account.forms import *
from django.contrib.auth.models import Group 


SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Calendar API Quickstart'

def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar-quickstart.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        #if flags:
        #    credentials = tools.run_flow(flow, store, flags)
        #else: # Needed only for compatability with Python 2.6
        credentials = tools.run(flow, store, None)
        print 'Storing credentials to ' + credential_path
    return credentials
	
def google_cal(request):
    """Shows basic usage of the Google Calendar API.

    Creates a Google Calendar API service object and outputs a list of the next
    10 events on the user's calendar.
    """
    credentials = get_credentials()
    service = build('calendar', 'v3', http=credentials.authorize(Http()))

    now = datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print 'Getting the upcoming 10 events'
    eventsResult = service.events().list(
        calendarId='primary', timeMin=now, maxResults=10, singleEvents=True,
        orderBy='startTime').execute()
    events = eventsResult.get('items', [])

    if not events:
        print 'No upcoming events found.'
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print start, event['summary']


register = template.Library() 

@register.filter(name='has_group') 
def has_group(user, group_name): 
	group = Group.objects.get(name=group_name) 
	return True if group in user.groups.all() else False

@property
def is_today(self):
    if date.today() == self.date:
        return True
    return False

def is_employee(user):
    return user.groups.filter(name='employees').exists()

class ActivitiesView(generic.DetailView):
	model = Gym
	template_name = 'account/gym/gym_activities.html'

	def get_context_data(self, **kwargs):
	    	context = super(ActivitiesView, self).get_context_data(**kwargs)
		now = datetime.datetime.now()
		seven_days = datetime.date.today() + timedelta(days=6)
		context['activities'] = GymActivity.objects.filter(gym=self.kwargs['pk']).filter(start__range=[now, seven_days]).order_by('start')
	    	#context['activities'] = GymActivity.objects.order_by('start')[:10]
		context['form'] = PostForm();
		carnet = ClientsVoucher.objects.filter(client=self.request.user.id).filter(date_order__lte=datetime.date.today()).filter(date_end__gte=datetime.date.today())
		if carnet.exists():
			context['has_carnet'] = True
        	return context

	def post(self, request, *args, **kwargs):
		if request.POST['google'] and is_employee(request.user):
			event = {
				'summary': 'Appointment',
				'location': 'Somewhere',
				'start': {
					'dateTime': '2011-06-03T10:00:00.000-07:00'
				},
				'end': {
					'dateTime': '2011-06-03T10:25:00.000-07:00'
				},
				'attendees': [
					{
						'email': 'attendeeEmail',
						# Other attendee's data...
					},
					# ...
				],
			}

			created_event = service.events().insert(calendarId='silowniamuscles.webowe@gmail.com', body=event).execute()
		else:
			if request.user.is_authenticated():
				carnet = ClientsVoucher.objects.filter(client=request.user.id).filter(date_order__lte=datetime.date.today()).filter(date_end__gte=datetime.date.today())
				if carnet.exists():
					gym_activity = GymActivity.objects.get(pk=request.POST['actId'])
					gym_activity.clients.add(request.user)
					gym_activity.save()
				else:
					url = reverse('gym_activities', kwargs={'pk': self.kwargs['pk']})
					return HttpResponseRedirect(url)
		url = reverse('gym_activities', kwargs={'pk': self.kwargs['pk']})
		return HttpResponseRedirect(url)
		#return HttpResponseRedirect(reverse('polls:vouchers'))

class GymView(generic.DetailView):
	model = Gym
	template_name = 'account/gym/gym.html'

	def get_context_data(self, **kwargs):
		context = super(GymView, self).get_context_data(**kwargs)
		return context

class GymsListView(generic.ListView):
	model = Gym
	template_name = 'account/gym/gyms.html'

	def get_context_data(self, **kwargs):
			context = super(GymsListView, self).get_context_data(**kwargs)
			context['objects'] = Gym.objects.all()
			context['users'] = CustomUser.objects.all()
			return context


def create_post(request):
    if request.method == 'POST':
        post_text = request.POST.get('the_post')
        response_data = {}

        post = Muscle(name=post_text)
        post.save()

        response_data['result'] = 'Create post successful!'
        response_data['postpk'] = post.pk
        response_data['name'] = post.name

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

