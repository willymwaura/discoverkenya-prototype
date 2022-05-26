
from django.db import models
from datetime import datetime

from pytz import timezone

# Create your models here.

class Feature(models.Model):
    region=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    experience=models.CharField(max_length=100)
    created=models.DateTimeField(default=datetime.now,blank=True)
    location=models.CharField(max_length=100,default="nairobi")
    weather=models.CharField(max_length=100,default="hot")
    def __str__(self):
        return '{}{}'.format(self.region,self.title)
class Map(models.Model):
    location=models.CharField(max_length=100,default="nairobi")
    destination=models.CharField(max_length=100,default="nairobi")
    distance=models.DecimalField(max_digits=10,decimal_places=2)
    def __str__(self):
        return '{}{}'.format(self.location,self.destination)
