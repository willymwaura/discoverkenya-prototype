from django.db import models
from datetime import datetime

from pytz import timezone

# Create your models here.
class Feature(models.Model):
    region=models.CharField(max_length=100,default ='central')
    title=models.CharField(max_length=100)
    experience=models.CharField(max_length=100)
    created=models.DateTimeField(default=datetime.now,blank=True)
    location=models.CharField(max_length=100,default="nairobi")
    weather=models.CharField(max_length=100,default="hot")
