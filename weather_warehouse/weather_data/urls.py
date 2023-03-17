from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('weather-data/', views.WeatherDataView.as_view(), name='weather_data'),
]