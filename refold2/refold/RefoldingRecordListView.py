from django.views.generic import ListView
from refold2.refold.models import RefoldingRecord
import urlparse

class RefoldingRecordListView(ListView):

    # model = RefoldingRecord      #implies -> queryset = models.Car.objects.all()
    context_object_name = "refoldingrecord_list"    #default is object_list
    paginate_by = 25  #and that's it !!
    protein = None

    def get_queryset(self):
        rr = RefoldingRecord.objects.all()
        
        self.protein = self.request.GET.get('protein')

        if self.protein:
            protein_unencoded = urlparse.unquote(self.protein)
            rr = rr.filter(construct__homologue__protein__name__icontains=protein_unencoded)
        
        return rr
        
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(RefoldingRecordListView, self).get_context_data(**kwargs)
        # Add in the publisher
        context['searchterm'] = self.protein
        return context
