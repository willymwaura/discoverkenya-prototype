from post.models import Feature
from django.shortcuts import render
from .models import Feature
from django.http.response import HttpResponse


# Create your views here.
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
    newexp=posts.experience+{newline}+ a

    posts.experience=newexp
    
    posts.save(update_fields=['experience'])
    return HttpResponse(" cat uploaded successfully,Thank you !")


