"""Файл обробки запитів до кінцевих точок (endpoints)."""
from django.shortcuts import render


def index(request):
    return render(request, '../templates/index.html')


def offers(request):
    return render(request, '../templates/offers.html')


def pricelist(request):
    return render(request, '../templates/pricelist.html')


def contacts(request):
    return render(request, '../templates/contacts.html')
