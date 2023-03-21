import pandas as pd
import re
from .clean_data import clean
from .fetch_data import fetch_data
import json

def check_date(df):
    date_str = df['date']
    date_format_regex = r"^\d{4}-\d{2}-\d{2}(T\d{2}:\d{2}:\d{2}Z)?$"
    is_valid_date_format = date_str.str.match(date_format_regex).all()
    if not is_valid_date_format:
        raise ValueError("Date column has invalid format")

def check_lat(df):
    valid_lats = df['coordinates.lat'].between(-90, 90).all
    if not valid_lats:
        raise ValueError("Latitude values outside of valid range")

def check_lon(df):
    # check longitudes
    valid_lons = df['coordinates.lon'].between(-180, 180).all()
    if not valid_lons():
        raise ValueError("Lontitude values outside of valid range")

def internal_validate(cleaned_df):
    df = clean(cleaned_df)
    check_date(df)    
    check_lat(df)
    check_lon(df)
    return True, "External validity check passed"

def external_validate(response):
    try:
        data = json.loads(response)
    except ValueError:
        return False, "Invalid JSON format"
    
    if 'version' not in data or 'user' not in data or 'dateGenerated' not in data or 'status' not in data or 'data' not in data:
        return False, 'Missing required field(s)'
    
    if data['status'] != 'OK':
        return False, f"Status code not OK: {data['status']}"
    
    for entry in data['data']:
        if 'parameter' not in entry or 'coordinates' not in entry:
            return False, 'Missing required field(s) in data'
        for coordinate in entry['coordinates']:
            if 'lat' not in coordinate or 'lon' not in coordinate or 'dates' not in coordinate:
                return False, 'Missing required field(s) in coordinates'
            for date in coordinate['dates']:
                if 'date' not in date or 'value' not in date:
                    return False, 'Missing required field(s) in dates'
                
    return True, "Internal validity check passed"
