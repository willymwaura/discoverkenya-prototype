from post.models import Feature
from django.shortcuts import render
from .models import Feature
from django.http.response import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from .models import Feature,Map
from .forms import MeasurementModelForm
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from .utils import get_geo, get_center_coordinates, get_zoom
import folium




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

def calculate_distance_view(request):
    # initial values
    distance = None
    destination = None
    
    obj = get_object_or_404(Map, id=1)
    form = MeasurementModelForm(request.POST or None)
    geolocator = Nominatim(user_agent='measurements')

    ip = '72.14.207.99'
    country, city, lat, lon = get_geo(ip)
    location = geolocator.geocode(city)

    # location coordinates
    l_lat = lat
    l_lon = lon
    pointA = (l_lat, l_lon)

    # initial folium map
    m = folium.Map(width=800, height=500, location=get_center_coordinates(l_lat, l_lon), zoom_start=8)
    # location marker
    folium.Marker([l_lat, l_lon], tooltip='click here for more', popup=city['city'],
                    icon=folium.Icon(color='purple')).add_to(m)

    if form.is_valid():
        instance = form.save(commit=False)
        destination_ = form.cleaned_data.get('destination')
        destination = geolocator.geocode(destination_)

        # destination coordinates
        d_lat = destination.latitude
        d_lon = destination.longitude
        pointB = (d_lat, d_lon)
        # distance calculation
        distance = round(geodesic(pointA, pointB).km, 2)

        # folium map modification
        m = folium.Map(width=800, height=500, location=get_center_coordinates(l_lat, l_lon, d_lat, d_lon), zoom_start=get_zoom(distance))
        # location marker
        folium.Marker([l_lat, l_lon], tooltip='click here for more', popup=city['city'],
                    icon=folium.Icon(color='purple')).add_to(m)
        # destination marker
        folium.Marker([d_lat, d_lon], tooltip='click here for more', popup=destination,
                    icon=folium.Icon(color='red', icon='cloud')).add_to(m)


        # draw the line between location and destination
        line = folium.PolyLine(locations=[pointA, pointB], weight=5, color='blue')
        m.add_child(line)
        
        instance.location = location
        instance.distance = distance
        instance.save()
    
    m = m._repr_html_()

    context = {
        'distance' : distance,
        'destination': destination,
        'form': form,
        'map': m,
    }

    return render(request, 'main.html', context)
