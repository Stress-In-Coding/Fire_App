from django.contrib import admin
from django.urls import path

from fire.views import HomePageView, WeatherConditionList, WeatherConditionCreateView, WeatherConditionUpdateView, WeatherConditionDeleteView,LocationList, LocationCreateView, LocationUpdateView, LocationDeleteView, IncidentList, IncidentCreateView, IncidentUpdateView, IncidentDeleteView, FireFightersList,FireFightersCreateView, FireFightersUpdateView, FireFightersDeleteView, FireStationList, FireStationCreateView, FireStationUpdateView, FireStationDeleteView, FireTrucksList, FireTrucksCreateView, FireTrucksUpdateView, FireTrucksDeleteView, ChartView, PieCountbySeverity, LineCountbyMonth, MultilineIncidentTop3Country, multipleBarbySeverity
from fire import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('dashboard_chart', ChartView.as_view(), name='dashboard-chart'),
    path('chart/', PieCountbySeverity, name='chart'),
    path('lineChart/', LineCountbyMonth, name='chart'),
    path('multilineChart/', MultilineIncidentTop3Country, name='chart'),
    path('multiBarChart/', multipleBarbySeverity, name='chart'),

    path('stations', views.map_station, name='map-station'),
    path('incident', views.map_incident, name='map-incident'),

    path('firestation_list', FireStationList.as_view(), name='firestation-list'),
    path('firestation_list/add', FireStationCreateView.as_view(), name='firestation-add'),
    path('firestation_list/<pk>', FireStationUpdateView.as_view(), name='firestation-update'),
    path('firestation_list/<pk>/delete', FireStationDeleteView.as_view(), name='firestation-delete'),

    path('firetrucks_list', FireTrucksList.as_view(), name='firetrucks-list'),
    path('firetrucks_list/add', FireTrucksCreateView.as_view(), name='firetrucks-add'),
    path('firetrucks_list/<pk>', FireTrucksUpdateView.as_view(), name='firetrucks-update'),
    path('firetrucks_list/<pk>/delete', FireTrucksDeleteView.as_view(), name='firetrucks-delete'),

    path('firefighters_list', FireFightersList.as_view(), name='firefighters-list'),
    path('firefighters_list/add', FireFightersCreateView.as_view(), name='firefighters-add'),
    path('firefighters_list/<pk>', FireFightersUpdateView.as_view(), name='firefighters-update'),
    path('firefighters_list/<pk>/delete', FireFightersDeleteView.as_view(), name='firefighters-delete'),

    path('incident_list', IncidentList.as_view(), name='incident-list'),
    path('incident_list/add', IncidentCreateView.as_view(), name='incident-add'),
    path('incident_list/<pk>', IncidentUpdateView.as_view(), name='incident-update'),
    path('incident_list/<pk>/delete', IncidentDeleteView.as_view(), name='incident-delete'),

    path('location_list', LocationList.as_view(), name='location-list'),
    path('location_list/add', LocationCreateView.as_view(), name='location-add'),
    path('location_list/<pk>', LocationUpdateView.as_view(), name='location-update'),
    path('location_list/<pk>/delete', LocationDeleteView.as_view(), name='location-delete'),

    path('weather_list', WeatherConditionList.as_view(), name='weather-list'),
    path('weather_list/add', WeatherConditionCreateView.as_view(), name='weather-add'),
    path('weather_list/<pk>', WeatherConditionUpdateView.as_view(), name='weather-update'),
    path('weather_list/<pk>/delete', WeatherConditionDeleteView.as_view(), name='weather-delete'),
]
