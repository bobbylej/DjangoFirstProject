from django.conf.urls import patterns, url
from account import views
import os.path
from django.conf import settings
from django.conf.urls.static import static

media_dir = os.path.join(os.path.dirname(__file__),'static')

urlpatterns = patterns('',
'''
	url(r'^vouchers/$', views.VouchersView.as_view(), name='vouchers'),
	url(r'^add_voucher/$', views.add_voucher, name='add_voucher'),
	url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root': media_dir}),
	url(r'^(?P<pk>\d+)/gym_activities/$', views.ActivitiesView.as_view(), name='gym_activities'),
	url(r'^gyms/$', views.GymsListView.as_view(), name='gyms'),
	url(r'^instructors/$', views.InstructorsListView.as_view(), name='instructors'),
	url(r'^(?P<pk>\d+)/gym/$', views.GymView.as_view(), name='gym')
'''
)
