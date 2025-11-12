# A serializer converts your database model into JSON format
from rest_framework import serializers
from weatherapp.models import WeatherData

class WeatherDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherData
        fields = ['id', 'date', 'region', 'parameter', 'value']

# This tells Django to convert WeatherData objects to JSON with these 5 fields.