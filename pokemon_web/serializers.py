import re
from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Pokemon,EntrenadorPK,Maquina_EntrenadorPK,Habilidades,Movimientos,Berries
from django.core.exceptions import ValidationError

class EntrenadorPKSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntrenadorPK
        fields = ('Fecha','ID','Username','Password','Password2','Imagen_Perfil','Dinero')
        
    def validate(self , attrs):    
            if attrs['Password'] != attrs['Password2']:
                raise ValidationError({"Password": "Password no Coinciden"})
            else:   
                return (attrs)

            
    
class MaquinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maquina_EntrenadorPK
        fields = ('ID','Nombre','Imagen_Perfil','Dinero','Dificultad')        
        
class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon        
        fields = ('ID_Entrenador','XP','ID_Maquina','ID','Nombre_Pokemon','Imagen_Pokemon','HP','Defensa','Peso','Altura','Estado','Nivel')
     
class HabilidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habilidades
        fields = ('Descripcion','Id_Pokemon','Nombre','Identificador')
         
class MovimientosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movimientos
        fields = ('Nombre','Id_Pokemon','Daño','Drenado','Cantidad','Efecto','Identificador_MO')         
        
class BerriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Berries
        fields = ('Descripcion','Nombre','Identificador','Cantidad','imagen_berrie','Costo','Efectoestadistico','EfectoEstado')