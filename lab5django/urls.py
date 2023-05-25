"""Варіанти звернень до кінцевих точок (endpoints) та їх прив'язка до методів, що оброблюють запити."""
from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('offers/', views.offers, name='offers'),
    path('pricelist/', views.pricelist, name='pricelist'),
    path('contacts/', views.contacts, name='contacts'),
]
