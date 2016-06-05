from django.conf.urls import patterns, include, url
from django.contrib import admin
from apka.views import *

urlpatterns = patterns('',
     (r'^$', main_page), 
     (r'^admin/', include(admin.site.urls))
)

