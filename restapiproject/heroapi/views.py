from django.shortcuts import render
from .models import Hero,Heroine
from rest_framework import viewsets
from .serializers import HeroSerializer,HeroineSerializer
# Create your views here.

class HeroViewSet(viewsets.ModelViewSet):
    queryset=Hero.objects.all()
    serializer_class=HeroSerializer

class HeroineViewSet(viewsets.ModelViewSet):
    queryset=Heroine.objects.all()
    serializer_class=HeroineSerializer
