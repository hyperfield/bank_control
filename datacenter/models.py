from django.db import models
import pytz
from datetime import datetime
from django.utils import timezone as tz

class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)
    
    def get_duration(self):
      moscow = pytz.timezone('Europe/Moscow')
      now = datetime.now()
      local_now = moscow.localize(now)
      if self.leaved_at is not None:
        delta = self.leaved_at - self.entered_at
      else:
        delta = local_now - self.entered_at
      return round(delta.total_seconds())

    def is_visit_long(self, minutes=60):
      return self.get_duration() >= minutes*60

    def __str__(self):
        return "{user} entered at {entered} {left}".format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved= "leaved at " + str(self.leaved_at) if self.leaved_at else "not leaved"
        )
