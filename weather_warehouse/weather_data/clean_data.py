import pandas as pd
import json

# returned columns: 
# date, value, parameter, coordinates.lat, coordinates.lon
def landing_clean(raw_json):
    raw_str = raw_json['data']
    df = pd.json_normalize(raw_str, record_path=['coordinates', 'dates'], meta=['parameter', ['coordinates', 'lat'], ['coordinates', 'lon']])
    return df 

# returned columns: 
# 'date', 'coordinates.lat', 'coordinates.lon', params ('sunrise:sql', 't_2m:C')
def clean(raw_json):
    # raw = open('./response.json')
    # raw = json.load(raw)
    # raw = json.dumps(raw)
    # raw_str = json.loads(raw)
    raw_str = raw_json['data']
    df = pd.json_normalize(raw_str, record_path=['coordinates', 'dates'], meta=['parameter', ['coordinates', 'lat'], ['coordinates', 'lon']])
    # columns: date, value, parameter, coordinates.lat, coordinates.lon
    pivoted_df = df.pivot(index=['date', 'coordinates.lat', 'coordinates.lon'], columns='parameter', values='value')
    pivoted_df = pivoted_df.reset_index() 
    # print(pivoted_df)  
    return pivoted_df


# Authentication is stored in settings.py
# d = fetch_data(api_key, '2023-03-16T00:00:00Z--2023-03-16T00:02:00Z:PT1H', 'sunrise:sql,t_2m:C', '50,10_40,20')
# clean(d)
