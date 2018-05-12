from django.conf.urls import patterns, include, url

from django.contrib import admin
from gstinfo.views import hello
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gstinfo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^hello/', 'gstinfo.views.hello', name = 'hello'),
    url(r'^home/', 'gstinfo.views.landing', name = 'home'),
    url(r'^valueStat/', 'gstinfo.views.valueStat', name = 'valueStat'),
    url(r'^uploadFile/', 'gstinfo.views.uploadData', name = 'uploadFile'),
    url(r'^getItemInfo', 'gstinfo.views.getItem', name = 'getItemInfo'),
    url(r'^showGraph', 'gstinfo.views.showGraph', name = 'showGraph'),
    url(r'^downloadFile', 'gstinfo.views.downloadData', name = 'downloadFile'),

)
