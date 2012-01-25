from django.conf.urls.defaults import patterns, include, url
from django.views.generic import DetailView, ListView
from refold.models import RefoldingRecord
from refold.RefoldingRecordListView import RefoldingRecordListView
from refold.RefoldingRecordByProteinListView import RefoldingRecordByProteinListView

from django.contrib import admin
admin.autodiscover()

core_urls = patterns(
    'refold2.refold.views',
    (r'^$', 'index'),
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
    
    (r'^refoldingrecord/digitalcontentdata/$',
        ListView.as_view(
            model=RefoldingRecord,
            template_name="refold/refoldingrecord_digitalcontentdata.html",
    )),    

    (r'^protein/(\w+)/$',
        RefoldingRecordByProteinListView.as_view(
        template_name="refold/refoldingrecord_byprotein_list.html"),
    ),

    url(r'^admin/', include(admin.site.urls)),
)
