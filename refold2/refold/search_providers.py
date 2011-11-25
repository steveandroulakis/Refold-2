# For django-completion https://github.com/coleifer/django-completion
# http://charlesleifer.com/blog/autocompletion-for-django-models-using-solr-redis-or-sql/
from completion.sites import AutocompleteProvider
from datetime import datetime

class ProteinSearchProvider(AutocompleteProvider):
    def get_title(self, obj):
        return obj.name

    def get_pub_date(self, obj):
        return datetime.now()

    def get_data(self, obj):
        return {'name': obj.name, 'protein_id': obj.protein_id}

    def get_queryset(self):
        return self.model._default_manager.all()
