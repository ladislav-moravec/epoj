from django.contrib import admin
from .models import Client, HomeAdress #Importujeme si modely

#Modely registrujeme
admin.site.register(Client)
admin.site.register(HomeAdress)
