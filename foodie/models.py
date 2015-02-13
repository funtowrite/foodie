import datetime

from django.db import models
from django.utils import timezone


class Vendor(models.Model):
    name = models.CharField(max_length=30)
    eventCount = models.IntegerField(default=0)

    def __unicode__(self):              
        return self.name

    class Meta:
        ordering = ('eventCount', 'name')

class Event(models.Model):
    name= models.CharField(max_length=100)
    startTime = models.DateTimeField('date start')
    endTime = models.DateTimeField('date end')
    location = models.CharField(max_length=200)
    vendors = models.ManyToManyField(Vendor)
    eventId = models.CharField(max_length=200)
    
    def __unicode__(self):             
        return self.name

    def isOver(self):
   		return self.endTime >= timezone.now().date() 
        #return self.endTime >= timezone.now().date() - datetime.timedelta(days=1)

    class Meta:
        ordering = ('name',)