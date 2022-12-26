from django.shortcuts import render
from django.http import HttpResponse

from Families.models import Family

def create_family(request):
   Family.objects.create( name='Maximo', age = 4, married=False)
   return HttpResponse('se creo un nuevo familiar')

def list_families(request):
    all_families = Family.objects.all()
    context= {
        'family': all_families
    }
    return render(request, 'families.html', context=context)