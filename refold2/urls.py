from django.conf.urls.defaults import patterns, include, url
from django.views.generic import ListView, DetailView
from refold.models import RefoldingRecord
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from django.core import serializers

urlpatterns = patterns('',

    (r'^refoldingrecords/$', ListView.as_view(
        model=RefoldingRecord,
    )),

    # url(r'^refoldingrecords/(?P<pk>\d+)/$',
    #     DetailView.as_view(
    #         model=RefoldingRecord,
    #         )),

    url(r'^admin/', include(admin.site.urls)),
)
