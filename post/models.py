
from django.db import models
from datetime import datetime

from pytz import timezone

# Create your models here.

class Feature(models.Model):
    region=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    experience=models.CharField(max_length=1000)
    created=models.DateTimeField(default=datetime.now,blank=True)
    nearby_town=models.CharField(max_length=100,default='kiambu')
    def __str__(self):
        return '{}{}'.format(self.region,self.title)

