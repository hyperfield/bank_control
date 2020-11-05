from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render

def visits_view():
    return Visit.objects.all()

visits = visits_view()
print(visits)