from django.shortcuts import render
import pandas as pd
import os
import sys
from requests.auth import HTTPBasicAuth
sys.path.append('weather_warehouse')
from rest_framework.views import APIView
from rest_framework.response import Response
from .fetch_data import fetch_data
from .clean_data import landing_clean, clean
from .validate_data import internal_validate, external_validate
from .models import Location, LandingLong, WindWide, TemperatureWide
from .insert_data import insert_long_table, insert_wide_table
from .serializer import LandingSerializer, LocationSerializer, WindSerializer, TemperatureSerializer

# Create your views here.
API_USERNAME = os.environ.get('API_USERNAME')
API_PASSWORD = os.environ.get('API_PASSWORD')
api_key = HTTPBasicAuth(API_USERNAME, API_PASSWORD)

class WeatherDataView(APIView):
    def get(self, request):
        times = request.GET.get('validdatetime')
        param = request.GET.get('parameters')
        loc = request.GET.get('location')
        form = request.GET.get('format')
        opt = request.GET.get('option_name')

        response = fetch_data(api_key, times, param, loc, form, opt)
        external_validate(response)
        landing_df = landing_clean(response)
        cleaned_df = clean(response)
        internal_validate(cleaned_df)
    
        dates_lst = []
        response_data = dict()
        for _, row in cleaned_df.iterrows():
            lan = row['coordinates.lan']
            lon = row['coordinates.lon']
            lan_lon = f"{lan},{lon}"
            location_obj, _ = Location.objects.get_or_create(location=lan_lon)
            dates = row['date']
            dates_lst.append(dates)
            insert_wide_table(cleaned_df, row, location_obj, dates)
        insert_long_table(landing_df)

        # query data upon request
        fields = cleaned_df.columns
        fields_s_ = pd.Series(fields)
        loc_queryset = Location.objects.filter(location=location_obj)
        lat = loc_queryset[0].lat
        lon = loc_queryset[0].lon
        loc_serializer = LocationSerializer(loc_queryset, many=True)
        response_data['Location'] = loc_serializer.data
        response_data['Latitude'] = lat
        response_data['Longitude'] = lon

        # fields_s_ = fields_s[~fields_s.columns.isin(['location'])]
        if fields_s_.str.startswith('wind').any():
            wind_fields = fields_s_[fields_s_.str.startswith('wind')]
            wind_queryset = WindWide.objects.filter(location=location_obj, datetime=dates_lst).values(wind_fields)
            serializer_class = WindSerializer
            wind_serializer = serializer_class(wind_queryset, many=True, fields=wind_fields)
            response_data['wind'] = wind_serializer.data
        if fields_s_.str.startswith('t_').any():
            temp_fields = fields_s_[fields_s_.str.startswith('t_')]
            temp_queryset = TemperatureWide.objects.filter(location=location_obj, datetime=dates_lst).values(temp_fields)
            serializer_class = TemperatureSerializer
            temp_serializer = serializer_class(temp_queryset, many=True, fields=temp_fields)
            response_data['Temperature'] = temp_serializer.data
        if not fields_s_.str.startswith('t_').any() and not fields_s_.str.startswith('wind').any():
            other_fields = fields_s_[~fields_s_.str.startswith('wind') & ~fields_s_.str.startswith('t_')]
            other_queryset = LandingLong.objects.filter(location=location_obj, datetime=dates_lst, parameter=other_fields).values(other_fields)
            landing_serializer = LandingSerializer(other_queryset, many=True, fields=other_fields)
            response_data['Other metrics'] = landing_serializer.data
 
        return Response(response_data)


