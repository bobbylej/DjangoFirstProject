# _*_ coding: utf-8 _*_
'''
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

from polls.models import *
from polls.forms import *
from django.contrib.auth.models import Group 


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

class ActivitiesView(generic.DetailView):
	model = Gym
	template_name = 'polls/gym/gym_activities.html'

	def get_context_data(self, **kwargs):
	    	context = super(ActivitiesView, self).get_context_data(**kwargs)
		now = datetime.datetime.now()
		seven_days = datetime.date.today() + timedelta(days=6)
		context['activities'] = GymActivity.objects.filter(gym=self.kwargs['pk']).filter(start__range=[now, seven_days]).order_by('start')
	    	#context['activities'] = GymActivity.objects.order_by('start')[:10]
		carnet = ClientsVoucher.objects.filter(client=self.request.user).filter(date_order__lte=datetime.date.today()).filter(date_end__gte=datetime.date.today())
		if carnet.exists():
			context['has_carnet'] = True
        	return context

	def post(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			carnet = ClientsVoucher.objects.filter(client=request.user).filter(date_order__lte=datetime.date.today()).filter(date_end__gte=datetime.date.today())
			if carnet.exists():
				gym_activity = GymActivity.objects.get(pk=request.POST['actId'])
				gym_activity.clients.add(request.user)
				gym_activity.save()
			else:
				url = reverse('polls:gym_activities', kwargs={'pk': self.kwargs['pk']})
				return HttpResponseRedirect(url)
		url = reverse('polls:gym_activities', kwargs={'pk': self.kwargs['pk']})
		return HttpResponseRedirect(url)
		#return HttpResponseRedirect(reverse('polls:vouchers'))

'''

