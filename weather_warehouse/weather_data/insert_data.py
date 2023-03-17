import pandas as pd
from .models import Location, LandingLong, WindWide, TemperatureWide

def insert_wide_table(cleaned_df, row, location_obj, dates):
    # for _, row in cleaned_df.iterrows():
    #     lan = row['coordinates.lan']
    #     lon = row['coordinates.lon']
    #     lan_lon = f"{lan},{lon}"
    #     location_obj, _ = Location.objects.get_or_create(location=lan_lon)
    #     dates = row['date']

    # insert into Wind table
    wind_obj, created = WindWide.objects.get_or_create(location=location_obj, datetime=dates)
    if 'wind_speed_10m:ms' in row:
        wind_speed_10m = row['wind_speed_10m:ms']
        wind_obj.wind_speed =wind_speed_10m
    if 'wind_dir_10m:d' in row:
        wind_dir_10m = row['wind_dir_10m:d']
        wind_obj.wind_dir=wind_dir_10m
    if 'wind_gusts_10m_1h:ms' in row:
        wind_gusts_10m_1h = row['wind_gusts_10m_1h:ms']
        wind_obj.wind_gusts_10m_1h=wind_gusts_10m_1h
    if 'wind_gusts_10m_24h:ms' in row:
        wind_gusts_10m_24h = row['wind_gusts_10m_24h:ms']
        wind_obj.wind_gusts_10m_24h=wind_gusts_10m_24h
    wind_obj.save()

    # insert into temperature table
    temp_obj, created = TemperatureWide.objects.get_or_create(location=location_obj, datetime=dates)
    if 't_2m:C' in row:
        temp = row['t_2m:C']
        temp_obj.temperature=temp
    if 't_max_2m_24h:C' in row:
        temp_max_24h = row['t_max_2m_24h:C']
        temp_obj.temperature_max_24h=temp_max_24h
    if 't_min_2m_24h:C' in row:
        temp_min_24h = row['t_min_2m_24h:C']
        temp_obj.temperature_min_24h=temp_min_24h
    temp_obj.save()

def insert_long_table(landing_df):
    for _, row in landing_df.iterrows():
        lan = row['coordinates.lan']
        lon = row['coordinates.lon']
        lan_lon = f"{lan},{lon}"
        location_obj, _ = Location.objects.get_or_create(location=lan_lon)
        dates = row['date']
        parameters =row['parameter']
        obj, created = LandingLong.objects.get_or_create(
            location=location_obj, 
            datetime=dates, 
            parameter=parameters,
            defaults={'value': row['value']})
        if not created:
            obj.value = row['value']
            obj.save()
            
