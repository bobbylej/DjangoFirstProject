from django.conf.urls import patterns, include, url
from django.contrib import admin
from polls import views as polls
from account import views as account

urlpatterns = patterns('', 
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^account/', include('account.urls', namespace="account")),
    #(r'^$', main_page),
    (r'^admin/', include(admin.site.urls)),
	url(r'^login_user/$', polls.login_user, name='login_user'),
	url(r'^instructors/$', account.InstructorsListView.as_view(), name='instructors'),
	url(r'^register/$', polls.register, name='register'),
	url(r'^user_acc/$', polls.user_acc, name='user_acc'),
	url(r'^update_profile/$', polls.update_profile, name='update_profile'),
	url(r'^change_password/$', polls.change_password, name='change_password'),
	url(r'^user_vouchers/$', polls.user_vouchers, name='user_vouchers'),
	url(r'^index/$', polls.index, name='index'),
	url(r'^vouchers/$', account.VouchersView.as_view(), name='vouchers'),
	url(r'^add_voucher/$', account.add_voucher, name='add_voucher'),
	url(r'^(?P<pk>\d+)/gym_activities/$', account.ActivitiesView.as_view(), name='gym_activities'),
	url(r'^gyms/$', account.GymsListView.as_view(), name='gyms'),
	url(r'^(?P<pk>\d+)/gym/$', account.GymView.as_view(), name='gym'),
	url(r'^create_post/$', account.create_post, name='create_post'),
	url(r'^registerface/(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$', polls.registerface, name='registerface'),
)
