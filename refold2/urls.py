from django.conf.urls.defaults import patterns, include, url
from django.views.generic import ListView #, DetailView
from refold.models import RefoldingRecord
from refold.RefoldingRecordByProteinListView import RefoldingRecordByProteinListView
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    (r'^refoldingrecord/$',
        ListView.as_view(
            model=RefoldingRecord,
    )),

    (r'^refoldingrecord/protein/(\w+)/$',
        RefoldingRecordByProteinListView.as_view(
        template_name="refold/refoldingrecord_byprotein_list.html"),
    ),

    # url(r'^refoldingrecords/(?P<pk>\d+)/$',
    #     DetailView.as_view(
    #         model=RefoldingRecord,
    #         )),

    url(r'^admin/', include(admin.site.urls)),
)
