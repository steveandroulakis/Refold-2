# Create your views here.
from django.http import HttpResponse, HttpResponseBadRequest
from django.template import RequestContext
from django.shortcuts import render_to_response
from completion import site
from refold2.refold.models import Protein
from refold2.refold.search_providers import ProteinSearchProvider

import json

def index(request):

    return render_to_response("refold/index.html", dict(),
                               context_instance=RequestContext(request))

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
