from tkinter import CASCADE
from django.db import models
from datetime import datetime

from pytz import timezone

# Create your models here.
class Region(models.Model):
    region=models.CharField(max_length=100)

    def __str__(self):
        return self.region
class Feature(models.Model):
    region=models.ForeignKey(Region,related_name='regions',on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    experience=models.CharField(max_length=100)
    created=models.DateTimeField(default=datetime.now,blank=True)
    location=models.CharField(max_length=100,default="nairobi")
    weather=models.CharField(max_length=100,default="hot")
    def __str__(self):
        return '{}{}'.format(self.region,self.title)

