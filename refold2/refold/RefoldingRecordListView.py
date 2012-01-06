from django.views.generic import ListView
from refold2.refold.models import RefoldingRecord

class RefoldingRecordListView(ListView):

    model = RefoldingRecord      #implies -> queryset = models.Car.objects.all()
    context_object_name = "refoldingrecord_list"    #default is object_list
    paginate_by = 25  #and that's it !!
