from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('search/', views.search, name='search'),
    path('manage/', views.manage, name='manage'),
    path('manage', views.home, name="manage"),
    path('login/', views.login, name = 'login'),
    path('create', views.m_form, name="create"),
    path('maker/', views.maker, name="maker"),
    path('contact/', views.contact, name="contact"),
    path('maker_sell/', views.maker_sell, name="maker_sell"),
    path('create/land', views.land_form, name="land"),
    path('create/plant', views.plant_form, name="plant"),
    path('api/get-season-info/<int:season_id>/', views.get_season_info, name='get_season_info'),
    path('api/get-land-by-season/<int:season_id>/', views.get_land_by_season, name='get-land-by-season'),
    path('api/get-land-info/<int:land_id>/', views.get_land_info, name='get-land-info'),
    path('api/get-plant-by-land/<int:land_id>/', views.get_plant_by_land, name='get-plant-by-land'),

]
