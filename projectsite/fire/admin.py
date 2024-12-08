from django.contrib import admin

from .models import Incident, Locations, Firefighters, FireStation, FireTruck, WeatherConditions



@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin):
    list_display = ("location", "date_time", "severity_level", "description")
    search_fields = ("location", "sever",)

@admin.register(Locations)
class LocationsAdmin(admin.ModelAdmin):
    list_display = ("name", "latitude", "longitude", "longitude", "address", "city", "country")
    search_fields = ("Location",)

@admin.register(Firefighters)
class FirefightersAdmin(admin.ModelAdmin):
    list_display = ("name", "rank", "experience_level", "station")
    search_fields = ("Firefighters",)

@admin.register(FireStation)
class FireFightersAdmin(admin.ModelAdmin):
    list_display = ("name", "latitude", "longitude", "address", "city","country")
    search_fields = ("Firefighters",)

@admin.register(FireTruck)
class FiretruckAdmin(admin.ModelAdmin):
    list_display = ("truck_number", "model", "capacity", "station")
    search_fields = ("Firetruck",)

@admin.register(WeatherConditions)
class WeatherConditionsAdmin(admin.ModelAdmin):
    list_display = ("incident", "temperature", "humidity", "wind_speed", "weather_description")
    search_fields = ("Weather",)
