from django.contrib import admin
from .models import Cliente, Estado, Etapa, Prospecto, Usuario

# Register your models here.

admin.site.register(Cliente)

admin.site.register(Estado)

admin.site.register(Etapa)

admin.site.register(Prospecto)

admin.site.register(Usuario)