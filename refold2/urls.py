from django.conf.urls.defaults import patterns, include, url
from django.views.generic import ListView, DetailView
from refold.models import RefoldingRecord
from refold.RefoldingRecordListView import RefoldingRecordListView
from refold.RefoldingRecordByProteinListView import RefoldingRecordByProteinListView
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

core_urls = patterns(
    'refold2.refold.views',
    (r'^protein/search/json/$', 'protein_search_json'),
)

urlpatterns = patterns('',

    (r'', include(core_urls)),

    (r'^refoldingrecord/$',
        RefoldingRecordListView.as_view()
    ),

    (r'^refoldingrecord/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=RefoldingRecord,
    )),

    (r'^protein/(\w+)/$',
        RefoldingRecordByProteinListView.as_view(
        template_name="refold/refoldingrecord_byprotein_list.html"),
    ),

    # url(r'^refoldingrecords/(?P<pk>\d+)/$',
    #     DetailView.as_view(
    #         model=RefoldingRecord,
    #         )),

    url(r'^admin/', include(admin.site.urls)),
)
