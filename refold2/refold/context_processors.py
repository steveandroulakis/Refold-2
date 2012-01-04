def refolding_record_count(request):
    from refold.models import RefoldingRecord
    return {'refolding_record_count': RefoldingRecord.objects.count()}
