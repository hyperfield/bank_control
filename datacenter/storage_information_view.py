from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
import pytz
from datetime import datetime
from django.utils import timezone as tz

def format_duration(duration):
    return '{}ч {:01d}мин'.format(duration//3600, duration//60 % 60)

def storage_information_view(request):
    visits_not_left = Visit.objects.filter(leaved_at__isnull=True) # Текущие визиты в хранилище
    moscow = pytz.timezone('Europe/Moscow')
    now = datetime.now()
    local_now = moscow.localize(now)

    visits = [] # Список визитов сотрудника в хранилище

    for visit in visits_not_left:
      person = visit.passcard.owner_name
      who_entered = Passcard.objects.get(owner_name=person)
      entered_at = tz.localtime(value=visit.entered_at, timezone=moscow)
      duration = format_duration(visit.get_duration())
      visits.append({"who_entered": who_entered, "entered_at": entered_at, "duration": duration, "is_strange": visit.is_visit_long()})

    context = {
        "non_closed_visits": visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
