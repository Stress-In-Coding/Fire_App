from django.contrib import admin
from django.urls import path

from fire.views import HomePageView, ChartView, PieCountbySeverity, LineCountbyMonth, MultilineIncidentTop3Country, multipleBarbySeverity, fire_incidents_map, delete_location, IncidentList, IncidentCreateView, IncidentRecords, IncidentListView, IncidentCreateView, IncidentUpdateView, IncidentDeleteView, firelocationListView, stationListView, firefighterListView, firetruckListView, weatherListView, StationCreateView, StationUpdateView, StationDeleteView, firefighterCreateView, firefighterUpdateView, firefighterDeleteView, firelocationCreateView, firelocationUpdateView, firelocationDeleteView, firetruckCreateView, firetruckUpdateView, firetruckDeleteView, weatherCreateView, weatherUpdateView, weatherDeleteView
weatherDeleteView
from fire import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('ChartJs', ChartView.as_view(), name='ChartJs'),
    path('PieChart/', PieCountbySeverity, name='chart'),
    path('lineChart/', LineCountbyMonth, name='chart'),
    path('multilineChart/', MultilineIncidentTop3Country, name='chart'),
    path('multiBarChart/', multipleBarbySeverity, name='chart'),
    path('stations', views.map_station, name='map-station'),
    path('fire_incidents_map/', views.fire_incidents_map, name='fire_incidents_map'),
    
    
    path('IncidentRecords/', IncidentListView.as_view(), name='Int-record'),
    path('IncidentRecords-add/', IncidentCreateView.as_view(), name='incidentrecord-add'),
    path('IncidentRecords/<int:pk>/', IncidentUpdateView.as_view(), name='Int-update'),
    path('IncidentRecords/<int:pk>/delete/', IncidentDeleteView.as_view(), name='Int-delete'),
    
    
    
    path('firelocations/', firelocationListView.as_view(), name='fire-location'),
    path('firelocation-add/', firelocationCreateView.as_view(), name='location-add'),
    path('firelocation/<int:pk>/', firelocationUpdateView.as_view(), name='location-update'),
    path('firelocation/<int:pk>/delete/', firelocationDeleteView.as_view(), name='location-delete'),
    
    
    
    path('firestation/', stationListView.as_view(), name='fire-station'),
    path('firestation-add/', StationCreateView.as_view(), name='station-add'),
    path('firestation/<int:pk>/', StationUpdateView.as_view(), name='station-update'),
    path('firestation/<int:pk>/delete/', StationDeleteView.as_view(), name='station-delete'),
    
    
    
    path('firefighters/', firefighterListView.as_view(), name='fire-fighters'),
    path('firefighters-add/', firefighterCreateView.as_view(), name='fighter-add'),
    path('firefighters/<int:pk>/', firefighterUpdateView.as_view(), name='fighter-update'),
    path('firefighters/<int:pk>/delete/', firefighterDeleteView.as_view(), name='fighter-delete'),
    
    
    path('firetrucks/', firetruckListView.as_view(), name='fire-truck'),
    path('firetrucks-add/', firetruckCreateView.as_view(), name='truck-add'),
    path('firetrucks/<int:pk>/', firetruckUpdateView.as_view(), name='truck-update'),
    path('firetrucks/<int:pk>/delete/', firetruckDeleteView.as_view(), name='truck-delete'),
    
    
    
    path('weathers/', weatherListView.as_view(), name='weather-condition'),
    path('weathers-add/', weatherCreateView.as_view(), name='wheather-add'),
    path('weathers/<int:pk>/', weatherUpdateView.as_view(), name='wheather-update'),
    path('weathers/<int:pk>/delete/', weatherDeleteView.as_view(), name='wheather-delete'),
    


  
 

    

]