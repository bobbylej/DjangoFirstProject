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

from account.models import *
#from account.forms import *

from account.gym import *
from polls.models import *


class VouchersView(generic.ListView):
	model = Voucher
	template_name = 'account/vouchers.html'

	def get_context_data(self, **kwargs):
	    	context = super(VouchersView, self).get_context_data(**kwargs)
	    	context['additions'] = Addition.objects.all()
		context['vouchers'] = Voucher.objects.order_by('price')
	    	# And so on for more models
        	return context

def add_voucher(request):
	if request.method == 'POST':
		if request.user.is_authenticated():
			if request.POST.get("buy"):
				voucher = Voucher.objects.get(name=request.POST['voucher_name'])
				ClientsVoucher.objects.create(client=request.user, voucher=voucher, date_order=datetime.datetime.now().date(), date_end=(datetime.datetime.now()+timedelta(days=voucher.days)).date())
				return HttpResponseRedirect(reverse('vouchers'))
	return HttpResponseRedirect(reverse('login_user'))



class InstructorsListView(generic.ListView):
	model = CustomUser
	template_name = 'account/instructors/instructors.html'

	def get_context_data(self, **kwargs):
		context = super(InstructorsListView, self).get_context_data(**kwargs)
		context['objects'] = CustomUser.objects.filter(employee_func__name='Instruktor')
		return context


