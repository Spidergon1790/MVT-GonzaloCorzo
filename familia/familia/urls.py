
from django.contrib import admin
from django.urls import path
from Families.views import create_family, list_families
urlpatterns = [
    path('admin/', admin.site.urls),
    path('create-family/',create_family),
    path('list-family/', list_families)
]
