from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from .storage_information_view import format_duration

def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    
    visits_log = Visit.objects.filter(passcard=passcard)
    visits = []
    for visit in visits_log:
      visits.append({"entered_at": visit.entered_at, "duration": format_duration(visit.get_duration()), "is_strange": visit.is_visit_long()})

    context = {
        "passcard": passcard,
        "this_passcard_visits": visits
    }
    return render(request, 'passcard_info.html', context)
