from django.db import models

# Create your models here.
class Location(models.Model):
    location = models.CharField(max_length=255, unique=True)

class LandingLong(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    datetime = models.DateTimeField(null=True, blank=True)
    parameter = models.CharField(max_length=255, null=True, blank=True)
    value = models.CharField(max_length=255, null=True, blank=True)
    class Meta:
        unique_together = ('location', 'datetime', 'parameter')

class WindWide(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    datetime = models.DateTimeField(null=True, blank=True)
    wind_speed = models.FloatField(null=True, blank=True)
    wind_dir = models.FloatField(null=True, blank=True)
    wind_gusts_10m_1h = models.FloatField(null=True, blank=True)
    wind_gusts_10m_24h = models.FloatField(null=True, blank=True)
    class Meta:
        unique_together = ('location', 'datetime')

class TemperatureWide(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    datetime = models.DateTimeField(null=True, blank=True)
    temperature = models.FloatField(null=True, blank=True)
    temperature_max_24h = models.FloatField(null=True, blank=True)
    temperature_min_24h = models.FloatField(null=True, blank=True)
    class Meta:
        unique_together = ('location', 'datetime')

# class PrecipitationLong(models.Model):
#     location = models.ForeignKey(Location, on_delete=models.CASCADE)
#     datetime = models.DateTimeField()
#     parameter = models.CharField(max_length=255)
#     value = models.FloatField()
#     # precip_1h = models.FloatField()
#     # precip_24h = models.FloatField()

# # class Sun(models.Model):
# #     location = models.ForeignKey(Location, on_delete=models.CASCADE)
# #     datetime = models.DateTimeField()
# #     uv = models.FloatField()
# #     sunrise = models.DateTimeField()
# #     sunset = models.DateTimeField()

# # class OtherMetrics(models.Model):
# #     location = models.ForeignKey(Location, on_delete=models.CASCADE)
# #     datetime = models.DateTimeField()
# #     msl = models.FloatField()
# #     weather_symbol_1h = models.FloatField()
# #     weather_symbol_24h = models.FloatField()
    
