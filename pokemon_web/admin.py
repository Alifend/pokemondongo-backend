from django.contrib import admin
from pokemon_web import models

# Register your models here.

admin.site.register(models.EntrenadorPK)
admin.site.register(models.Maquina_EntrenadorPK)
admin.site.register(models.Pokemon)
admin.site.register(models.Habilidades)
admin.site.register(models.Movimientos)
admin.site.register(models.Berries)
