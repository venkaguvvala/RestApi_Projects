from rest_framework import serializers
from .models import Hero,Heroine

class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model=Hero
        fields='__all__'

class HeroineSerializer(serializers.ModelSerializer):
    class Meta:
        model=Heroine
        fields='__all__'
