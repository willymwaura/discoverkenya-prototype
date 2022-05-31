from post.models import Feature
from django.shortcuts import render,redirect
from .models import Feature
from django.http.response import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.shortcuts import render, get_object_or_404
import requests





def index(request):
    post=Feature.objects.all()
    return render(request,"index.html",{"object_list":post})

def posts(request,pk):
    posts=Feature.objects.get(id=pk)
    return render (request,"posts.html",{"posts":posts})


def addexperience(request,pk):
    a=request.POST['added']
    posts=Feature.objects.get(id=pk)
    newline='\n'
    newexp=posts.experience+ a

    posts.experience=newexp
    
    posts.save(update_fields=['experience'])
    return HttpResponse(" experience added  successfully,Thank you !,We love you")


def test(request):
    return render(request,'test.html')

def perregion(request):
    a=request.POST.get('added',False)
    b=Feature.objects.filter(region=a)
    return render(request,"correct.html",{"object_list":b})
def addfeature(request):
    a=request.POST['title']
    b=request.POST['experience']
    c=request.POST['location']
    d=request.POST['weather']
    f=request.POST['region']
    e=Feature(title=a,experience=b,location=c,weather=d,region=f)
    e.save()
    return HttpResponse(" tourist site  added successfully,Thank you ! We love you")

#Basic view for routing 

def show_map(request,pk):
    site=Feature.objects.get(id=pk)
    site_name=site.title
    url="https://www.google.com/maps/dir/?api=1&destination="
    mode="&travelmode=driving"

    return redirect (url+site_name+mode)
