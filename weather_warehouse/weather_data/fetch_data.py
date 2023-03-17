import requests
import json
import sys
import pandas as pd
from requests.auth import HTTPBasicAuth
sys.path.append('weather_warehouse')
import os

# Authentication is stored in settings.py
API_USERNAME = os.environ.get('API_USERNAME')
API_PASSWORD = os.environ.get('API_PASSWORD')
api_key = HTTPBasicAuth(API_USERNAME, API_PASSWORD)

def fetch(api_key, times, parameters, locations, format='json', opt_params='model=mix&mask=land'):
    base_url = 'https://api.meteomatics.com'
    request_url = f'{base_url}/{times}/{parameters}/{locations}/{format}?{opt_params}'   
    response = requests.get(request_url, auth=api_key)

    if response.status_code == 200:
        print('Fetch successfully!')
        json_data = response.json()
        df = pd.DataFrame(json_data)
        with open('response.json', 'w') as file:
            json.dump(json_data, file)
            print('Saved!')
    else:
        print('Fetch not success!')

    return response.json()

# ans = fetch_data(api_key, '2023-03-16T00:00:00Z--2023-03-16T00:02:00Z:PT1H', 'sunrise:sql,t_2m:C', '50,10_40,20')