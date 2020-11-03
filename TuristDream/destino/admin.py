from django.contrib import admin

# Register your models here.

from . models import Ciudad , Destino

admin.site.register(Ciudad)
admin.site.register(Destino)
