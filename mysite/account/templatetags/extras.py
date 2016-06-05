#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from django import template
from django.contrib.sites.models import Site
from django.utils.http import urlquote_plus
from django.contrib.auth.models import Group

register = template.Library() 

@register.filter
def google_calendarize(event):
	st = event.start
	en = event.end
	tfmt = '%Y%m%dT%H%M%S'

	dates = '%s%s%s' % (st.strftime(tfmt), '%2F', en.strftime(tfmt))
	
	name = urlquote_plus(event.activity.name + ' - siłownia MUSCLES')

	s = ('http://www.google.com/calendar/event?action=TEMPLATE&' +
         'text=' + name + '&' +
         'dates=' + dates + '&' +
         'sprop=website:' + urlquote_plus(Site.objects.get_current().domain))
		 
	if event.gym.no_local:
		temp = urlquote_plus(event.gym.city + ', ' + event.gym.street + ' ' + event.gym.no_building + '/' + event.gym.no_local)
	else:
		temp = urlquote_plus(event.gym.city + ', ' + event.gym.street + ' ' + event.gym.no_building)
			
	#s = s + '&location=' + urlquote_plus(event.gym.city + ' ' + event.gym.street + ' ' + event.gym.no_building + '/' + event.gym.no_local)
	s = s + '&location=' + temp

	return s + '&trp=false'

google_calendarize.safe = True