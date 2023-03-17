from rest_framework import serializers
from .models import Location, LandingLong, WindWide, TemperatureWide

class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop("fields", None)
        super().__init__(*args, **kwargs)
        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)
    
    class Meta:
        abstract = True

class LocationSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
    def get_lat(self, obj): 
        return obj.location.split(',')[0]
    def get_lon(self, obj): 
        return obj.location.split(',')[1]

class LandingSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = LandingLong
        fields = '__all__'

class WindSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = WindWide
        fields = '__all__'

class TemperatureSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = TemperatureWide
        fields = '__all__'
