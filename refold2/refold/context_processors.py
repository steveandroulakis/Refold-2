def refolding_record_count(request):
    from refold2.refold.models import RefoldingRecord
    return {'refolding_record_count': RefoldingRecord.objects.count()}
