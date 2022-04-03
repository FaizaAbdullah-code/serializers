from django.shortcuts import render
from .models import Heros, bioData
from .serializers import Heroserializers, Biodataserializers
from rest_framework import viewsets
import requests
# Create your views here.

def index(request):
    response= requests.get('http://127.0.0.1:8000/heroes/').json()
    return render(request,'index.html',{'response':response})

def biodata(request):
    responsedata = requests.get('http://127.0.0.1:8000/bioData/').json()    
    return render(request, 'biodata.html', {'responsedata': responsedata})

class HeroViewSet(viewsets.ModelViewSet):
    queryset = Heros.objects.all().order_by('name')
    serializer_class = Heroserializers

class BiodataViewSet(viewsets.ModelViewSet):
    queryset = bioData.objects.all().order_by('rollno')
    serializer_class =  Biodataserializers   

