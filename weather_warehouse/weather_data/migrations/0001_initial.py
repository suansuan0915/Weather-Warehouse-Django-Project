# Generated by Django 3.2.12 on 2023-03-16 01:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=255, unique=True)),
                ('lan', models.FloatField()),
                ('lon', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='WindLong',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('wind_speed', models.FloatField()),
                ('wind_dir', models.FloatField()),
                ('wind_gusts_10m_1h', models.FloatField()),
                ('wind_gusts_10m_24h', models.FloatField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weather_data.location')),
            ],
        ),
        migrations.CreateModel(
            name='WeatherWide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('parameter', models.CharField(max_length=255, unique=True)),
                ('value', models.FloatField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weather_data.location')),
            ],
        ),
        migrations.CreateModel(
            name='TemperatureLong',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('temperature', models.FloatField()),
                ('temperature_max_24h', models.FloatField()),
                ('temperature_min_24h', models.FloatField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weather_data.location')),
            ],
        ),
        migrations.CreateModel(
            name='PrecipitationLong',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('precip_1h', models.FloatField()),
                ('precip_24h', models.FloatField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weather_data.location')),
            ],
        ),
    ]
