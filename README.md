# Weather-Warehouse-Django-Project
 
## Project Description
This Django project builds a data warehouse based on the Meteomatics Weather API.\
[Link for Meteomatics Weather API](https://www.meteomatics.com/en/api/getting-started/)

The data warehouse would query weather data from Meteomatics API accroding to the request sent by users. \
Users can make API calls to get access to different kinds of weather data for various datetimes and latitude, longitute they want. 

#### Technologies Used
Django-REST-Framework\
Python\
PostgreSQL

## Project Structure
```
.
├── README.md
└── weather_warehouse
    ├── manage.py
    ├── response.json
    ├── weather_data
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── clean_data.py
    │   ├── fetch_data.py
    │   ├── insert_data.py
    │   ├── migrations
    │   ├── models.py
    │   ├── serializer.py
    │   ├── tests.py
    │   ├── urls.py
    │   ├── validate_data.py
    │   └── views.py
    └── weather_warehouse
        ├── __init__.py
        ├── asgi.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py
```


## Usage

#### Example of API Request URL
`http://localhost:8000/api/weather-data/validdatetime='2023-03-16T00:00:00Z--2023-03-17T00:00:00Z:PT1H'&parameters='sunrise:sql,t_2m:C'&location='50,10_40,20'`

#### Fields in Request URL
- Mandatory Parameters:\
[Details reference](https://www.meteomatics.com/en/api/available-parameters/)\
`validdatetime`: datetime or datetime range for the data.\
`parameters`: metric types of weather data, including metrics of wind, temperature, precipitation, sunlight, sealevel, etc.\
  - Wind metrics: `wind_speed_10m:ms`, `wind_dir_10m:d`, `wind_gusts_10m_1h:ms`, `wind_gusts_10m_24h:ms`
  - Temperature metrics: `t_2m:C`, `t_max_2m_24h:C`, `t_min_2m_24h:C`
  - Sealevel metrics: `msl_pressure:hPa`
  - Precipitation metrics: `precip_1h:mm`, `precip_24h:mm`
  - Weather symbols: `weather_symbol_1h:idx`, `weather_symbol_24h:idx`
  - Sunlight metrics: `uv:idx`, `sunrise:sql`, `sunset:sql`\
`location`: latitude and longitute of the location(s).
- Optional Parameters:\
[Details reference](https://www.meteomatics.com/en/api/request/optional-parameters/)\
'option_name': optional parameters of data. 
  - `source`
  - `calibrated`
  - `mask`
  - `ens_select`
  - `cluster_select`
  - `timeout`
  - `route`
  
