from django.http import HttpResponse
from django.shortcuts import render

def list_families(request):
    return HttpResponse('Listado de familia')


