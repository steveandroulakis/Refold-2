# Create your views here.
from django.http import HttpResponse, HttpResponseBadRequest
from completion import site
from refold.models import Protein
from refold.search_providers import ProteinSearchProvider

import json

def protein_search_json(request):
    if 'term' in request.GET:
        term = request.GET['term']

        site.register(Protein, ProteinSearchProvider)

        result_dict = site.suggest(term)

        return HttpResponse(json.dumps(result_dict), mimetype="application/json")
    else:
        response_data = dict()
        response_data['result'] = 'failed'
        response_data['message'] = "Need to supply a GET variable 'term'"
        return HttpResponseBadRequest(json.dumps(response_data), mimetype="application/json")
