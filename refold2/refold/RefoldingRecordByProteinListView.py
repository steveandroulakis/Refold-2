from django.views.generic import ListView
from refold.models import RefoldingRecord, Protein
from django.shortcuts import get_object_or_404

class RefoldingRecordByProteinListView(ListView):

    context_object_name = "refoldingrecords_byprotein"

    def get_queryset(self):
        self.protein = get_object_or_404(Protein, protein_id=self.args[0])
        return RefoldingRecord.objects.filter(construct__homologue__protein__protein_id=self.protein.protein_id)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(RefoldingRecordByProteinListView, self).get_context_data(**kwargs)
        # Add in the publisher
        context['searchterm'] = self.protein
        return context
