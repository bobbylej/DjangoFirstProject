from django.conf.urls import patterns, url
from polls import views
import os.path
from django.conf import settings
from django.conf.urls.static import static

media_dir = os.path.join(os.path.dirname(__file__),'static')

urlpatterns = patterns('',
	#url(r'^$', views.index, name='index'),
	#url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
	#url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
	#url(r'^$', views.IndexView.as_view(), name='index'),
	#url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
	#url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
	#url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
	#url(r'^vouchers/$', views.VouchersView.as_view(), name='vouchers'),
	#url(r'^add_voucher/$', views.add_voucher, name='add_voucher'),
	#url(r'^(?P<pk>\d+)/gym_activities/$', views.ActivitiesView.as_view(), name='gym_activities'),
'''
	url(r'^login_user/$', views.login_user, name='login_user'),
	url(r'^register/$', views.register, name='register'),
	url(r'^user_acc/$', views.user_acc, name='user_acc'),
	url(r'^index/$', views.index, name='index'),
	url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root': media_dir}),
'''
)
