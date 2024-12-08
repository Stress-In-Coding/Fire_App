from django.forms import ModelForm
from django import forms
from .models import Locations, Incident, FireStation, Firefighters, FireTruck, WeatherConditions

class LocationForm(ModelForm):
    class Meta:
        model= Locations
        fields = "__all__"
        widgets = {
            'date_joined': forms.DateInput(attrs={'type':'date'})
        }

class IncidentForm(ModelForm):
    class Meta:
        model= Incident
        fields = "__all__"
        widgets = {
            'date_joined': forms.DateInput(attrs={'type':'date'})
        }
        

class FireStationForm(ModelForm):
    class Meta:
        model= FireStation
        fields = "__all__"

class FireFightersForm(ModelForm):
    class Meta:
        model= Firefighters
        fields = "__all__"

class FireTruckForm(ModelForm):
    class Meta:
        model= FireTruck
        fields = "__all__"

class WeatherConditonForm(ModelForm):
    class Meta:
        model= WeatherConditions
        fields = "__all__"
        