# Generated by Django 3.2.12 on 2023-03-17 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather_data', '0003_landinglong_location_temperaturewide_windwide'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landinglong',
            name='datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='landinglong',
            name='parameter',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='landinglong',
            name='value',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='temperaturewide',
            name='datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='temperaturewide',
            name='temperature',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='temperaturewide',
            name='temperature_max_24h',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='temperaturewide',
            name='temperature_min_24h',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='windwide',
            name='datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='windwide',
            name='wind_dir',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='windwide',
            name='wind_gusts_10m_1h',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='windwide',
            name='wind_gusts_10m_24h',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='windwide',
            name='wind_speed',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='landinglong',
            unique_together={('location', 'datetime', 'parameter')},
        ),
        migrations.AlterUniqueTogether(
            name='temperaturewide',
            unique_together={('location', 'datetime')},
        ),
        migrations.AlterUniqueTogether(
            name='windwide',
            unique_together={('location', 'datetime')},
        ),
    ]
