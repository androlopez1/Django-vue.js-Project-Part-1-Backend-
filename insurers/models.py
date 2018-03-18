import datetime
from django.db import models
from django.utils import timezone

class RiskType(models.Model):
    risk_name = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    
    def was_published_recently(self):      
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    
    def __str__(self):
        return self.risk_name

class RiskField(models.Model):
    TEXT = 'text'
    NUMBER = 'number'
    DATE = 'date'
    ENUM = 'enum'

    FIELD_OPTIONS = (
        (TEXT, 'text'),
        (NUMBER, 'number'),
        (DATE, 'date'),
        (ENUM, 'enum'),
    )

    risk = models.ForeignKey(RiskType, related_name='fields', on_delete=models.CASCADE)
    field_name = models.CharField(max_length=200)
    field_type = models.CharField(max_length=10, choices=FIELD_OPTIONS)
    value = models.CharField(max_length=20)

    class Meta:
        unique_together = ('risk','value')
        ordering = ['value']


