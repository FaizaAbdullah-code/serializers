from rest_framework import serializers
from .models import Heros, bioData

class Heroserializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Heros
        fields = ('name', 'department')

class Biodataserializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = bioData
        fields = ('name', 'rollno', 'section', 'year')    