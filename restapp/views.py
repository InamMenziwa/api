from django.shortcuts import render
from rest_framework import generics, status, viewsets
from .models import Titles
from .serializers import Blogserializer
import csv
from rest_framework.response import Response
import requests 

class Blogcreation(generics.ListCreateAPIView):
    queryset = Titles.objects.all()
    serializer_class = Blogserializer

def Homepage(request):
    response = requests.get('https://mysite-8o30.onrender.com/api/data/')
    data = response.json() 
    return render(request, 'restapp/index.html', {"data": data})
    



