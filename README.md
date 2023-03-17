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

## Usage

#### Example of API call URL
`http://localhost:8000/api/weather-data/validdatetime='2023-03-16T00:00:00Z--2023-03-17T00:00:00Z:PT1H'&parameters='sunrise:sql,t_2m:C'&location='50,10_40,20'`

#### Fields in URL
- Mandatory Parameters:\
`validdatetime`: datetime or datetime range for the data.\
`parameters`: metric types of weather data, including metrics of wind, temperature, precipitation, sunlight, sealevel, etc.\
  - `wind`
`location`: latitude and longitute of the location(s).
- Optional Parameters:\
'option_name': optional parameters of data.
  - `source`: select a specific source for weather data.
  - `calibrated`: enables the calibration of historical and nowcast (first 6 hours of forecast) data with actual station measurements. The influence of a station at a certain location decreases with increasing distance from the station.
  - `mask`: Mask a parameter to only be valid on land or sea.
  - `ens_select`: When explicitly requesting data based on an ensemble model using the 'model' parameter (e.g. ecmwf-ens), you can specify the member or aggregate to return via this parameter.
  - `cluster_select`: By using `ecmwf-ens-cluster`, you can query cluster data based on ECMWF.
  
