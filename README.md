# Weather-Warehouse-Django-Project
 
## Project Description
This Django project builds a data warehouse based on the Meteomatics Weather API.\
[Link for Meteomatics Weather API](https://www.meteomatics.com/en/api/getting-started/)

The data warehouse would query weather data from Meteomatics API accroding to the API request sent by users. \
Users can make API calls to get access to different kinds of weather data for various datetimes and latitude, longitute they want. 

#### Technologies Used
Django-REST-Framework\
Python\
PostgreSQL

## Project Architecture
```
.
├── README.md
└── weather_warehouse/
    ├── manage.py
    ├── requirements.txt
    ├── weather_data/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── clean_data.py
    │   ├── fetch_data.py
    │   ├── insert_data.py
    │   ├── migrations/
    │   ├── models.py
    │   ├── serializer.py
    │   ├── tests.py
    │   ├── urls.py
    │   ├── validate_data.py
    │   └── views.py
    └── weather_warehouse/
        ├── __init__.py
        ├── asgi.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py
```

manage.py, requirements.txt, weather_warehouse folder, and weather_data folder consist the project.
- weather_warehouse folder
  - `settings.py`\
  Specifying settings and environment variables for the project.
  - `urls.py`\
  Acting as routers for request urls.
- weather_data folder
  - `fetch_data.py`\
  Retrieving raw data from Meteomatics API, which is in json format.
  - `clean_data.py`\
  Applying *pandas* transformation to the retrieved json object to get a pandas dataframe.
  - `models.py`\
  Specifying schema for tables in the PostgreSQL database here.
  - `validate_data.py`\
  Validating data internally and externally.
  - `views.py`\
  Handling incoming request and returning responses to users.
  - `serializer.py`\
  Serializing and deserializing django model objects and json objects.
  - `urls.py`\
  Acting as routers for weather_data.
  
#### Database Introduction
4 tables are created in the PostgreS database:
- `Location` Table\
  Storing lat and lon information.\
  `location`: in `lan,lon`format. Foreign keys for other tables.
- `LandingLong` Table\
  Long format table.\
  Acting as the landing table for all data.\
  `datetime`\
  `location`\
  `parameter`\
  `value`\
  Primary Key: (`datetime`, `location`, `parameter`)
- `WindWide` Table\
  Wide format table.\
  `datetime`\
  `location`\
  `wind_speed`\
  `wind_dir`\
  `wind_gusts_10m_1h`\
  `wind_gusts_10m_24h`\
  Primary Key: (`datetime`, `location`)
- `TemperatureWide` Table\
  Wide format table.\
  `datetime`\
  `location`\
  `temperature`\
  `temperature_max_24h`\
  `temperature_min_24h`\
  Primary Key: (`datetime`, `location`)
  
##### Pros&Cons of Schema
Pros:
- Data is stored in both "long" and "wide" formats, making it suitable for various analytical needs (e.g: Long format tables are more suitable for analysis that involves aggregating or summarizing data, while wide format tables are good for statistical analysis and modeling).
- The schema is normalized for different locations and datetimes, which reduces data redundancy and improves data integrity.
- Separate tables for locations and different catogories of weather parameters simplify the schema and improve its maintainability.
- Long format table acting as landing table makes it easier to check general validity when data arrives from outside API.

Cons:
- Limited scalability: Storing both "long" and "wide" formats can lead to increased storage requirements. Besides, large volumes of real-time updates can cause storage problem, especially for the relational database.
- Data redundancy: Redundacy is stilled provided here, like repeated "location" and "datetimes".
- Performance issues: The relational database table schema can suffer from slow query times and bad database performance, particularly when dealing with complex queries. 
- Limited flexibility: Meteomatics API also provides graphs of weather data. However, the database schema here don't allow us to store those unstructured data.
- Complexity: The table schema and relationships between tables can also be quite complex if we introduce more detailed metrics.

## Usage

#### Example of API Request URL
`http://localhost:8000/api/weather-data/validdatetime='2023-03-16T00:00:00Z--2023-03-17T00:00:00Z:PT1H'&parameters='sunrise:sql,t_2m:C'&location='50,10_40,20'`

#### Fields in Request URL
- Mandatory Parameters:\
[Details reference](https://www.meteomatics.com/en/api/available-parameters/)\
`validdatetime`: datetime or datetime range for the data.\
`location`: latitude and longitute of the location(s).\
`parameters`: metric types of weather data, including metrics of wind, temperature, precipitation, sunlight, sealevel, etc.\
  - Wind metrics: `wind_speed_10m:ms`, `wind_dir_10m:d`, `wind_gusts_10m_1h:ms`, `wind_gusts_10m_24h:ms`
  - Temperature metrics: `t_2m:C`, `t_max_2m_24h:C`, `t_min_2m_24h:C`
  - Sealevel metrics: `msl_pressure:hPa`
  - Precipitation metrics: `precip_1h:mm`, `precip_24h:mm`
  - Weather symbols: `weather_symbol_1h:idx`, `weather_symbol_24h:idx`
  - Sunlight metrics: `uv:idx`, `sunrise:sql`, `sunset:sql`
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
  
## Further Thinking
Given the project is required to be submitted into 72 hours, some functionalities are yet to be explored, including:\
- A user-friendly Interface. Field formats in the request url. Different metrics accept various format of values, users may need to remind themselves of different value formats and use correct value formats. If time allows, `static` folder can be added to include CSS and HTML templates, which provide users with buttons to select for their API request, instead of manually typing.
- Request file format. We only include json format here. If time allows, more format would be accepted.
- Real-time update of data warehouse. Now the database would be updated when users send requests. We can add a `realtime_update.py` so that the application can automatically download and update data in the database during specific intervals.
