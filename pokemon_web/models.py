from typing import Tuple
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from django.utils import timezone
from django.core.exceptions import ValidationError

# Create your models here.

#_____________________________________________________________________________________________
#Entrenador

class EntrenadorPK (models.Model):
    Fecha = models.DateField("Fecha (Año/Mes/Dia)", default = timezone.now)
    ID = models.CharField(primary_key= True,max_length=40,null=False,default="0")
    Username = models.CharField(max_length = 50,unique=True)
    Password = models.CharField(max_length=20,null=False)
    Password2 = models.CharField(max_length=20,null=False)
    Imagen_Perfil = models.URLField(max_length = 900)
    Dinero = models.IntegerField()


    #Metada
    class Meta:
        ordering = ["Fecha"]

        
    def __str__(self):
        return   self.Username


#_____________________________________________________________________________________________
#Maquina

class Maquina_EntrenadorPK (models.Model):
    StatusMaquina=(
        (('Facil','Facil')),
        (('Medio','Medio')),
        (('Dificil','Dificil')),
         )

    ID = models.CharField(primary_key= True,max_length=40,null=False,default= "0")
    Nombre = models.CharField(max_length = 50,null=False)
    Imagen_Perfil = models.URLField(max_length = 900)
    Dinero = models.IntegerField()
    Dificultad = models.CharField(choices= StatusMaquina, default="Facil", max_length=15)

     #Metada
    class Meta:
        ordering = ["ID"]

    def __str__(self):
        return   self.Nombre

#_____________________________________________________________________________________________
#Pokemon

    
class Pokemon (models.Model):
    
    StatusPokemon=(
        (('Confuso','Confuso')),
        (('Dormido','Dormido')),
        (('Quemado','Quemado')),
        (('Congelado','Congelado')),
        (('Paralizado','Paralizado')),
        (('Normal','Normal'))        
        )

    ID_Entrenador = models.ForeignKey(EntrenadorPK,default="0",on_delete=models.CASCADE)
    ID_Maquina = models.ForeignKey(Maquina_EntrenadorPK,default="0",on_delete=models.CASCADE)
    ID = models.CharField(primary_key=True,max_length=2000,null=False)
    Nombre_Pokemon = models.CharField(max_length=20,null=False)
    Imagen_Pokemon = models.URLField(max_length = 900,null=False)
    XP = models.IntegerField(null=False,default=1)
    HP = models.IntegerField(null = False,default = 1)
    Defensa = models.IntegerField(null = False,default = 1)
    Peso = models.IntegerField(null = False,default = 1)
    Altura = models.IntegerField(null = False,default = 1)
    Estado = models.CharField(max_length=20, choices= StatusPokemon, default='Normal')
    Nivel = models.IntegerField(null = False,default = 1)
    
    
         #Metada
    class Meta:
        ordering = ["ID"]

    def __str__(self):
        return   self.Nombre_Pokemon

#_____________________________________________________________________________________________
#Habilidades


class Habilidades (models.Model):
    Descripcion = models.CharField(max_length=400)
    Id_Pokemon = models.ForeignKey(Pokemon,on_delete=CASCADE)
    Nombre = models.CharField(max_length=20,null=False)
    Identificador = models.CharField(primary_key=True,max_length=200)

         #Metada
    class Meta:
        ordering = ["Nombre"]

    def __str__(self):
        return   self.Nombre
    
    
#_____________________________________________________________________________________________
#Movimientos
    
    
class Movimientos (models.Model):
    StatusMovimiento=(
        (('Confuso','Confuso')),
        (('Dormido','Dormido')),
        (('Quemado','Quemado')),
        (('Congelado','Congelado')),
        (('Paralizado','Paralizado')),
        (('Normal','Normal')),(('Sin Efecto','Sin Efecto'))        
        )
    
    Nombre = models.CharField(max_length=20,null=False)
    Id_Pokemon = models.ForeignKey(Pokemon,on_delete=CASCADE)
    Daño = models.IntegerField(default=1)
    Drenado = models.IntegerField(default=0) 
    Cantidad = models.IntegerField(default=1)
    Efecto = models.CharField(max_length=20, choices= StatusMovimiento, default= "Sin Efecto")
    Identificador_MO = models.CharField(primary_key=True,max_length=200)
    aumentos = models.IntegerField(default=0)    
        
             #Metada
    class Meta:
        ordering = ["Nombre"]

    def __str__(self):
        return   self.Nombre

#_____________________________________________________________________________________________
#Berries


class Berries (models.Model):
    StatusBerries=(
        (('Normal','Normal')),(('Sin Efecto','Sin Efecto'))        
        )

    Descripcion = models.CharField(max_length=400)
    Nombre = models.CharField(max_length=20,null=False)
    Identificador = models.CharField(primary_key=True,max_length=200)
    Cantidad = models.IntegerField(default=1)
    imagen_berrie = models.URLField(max_length=900)
    Costo = models.IntegerField(default=1)
    Efectoestadistico = models.IntegerField(default=0)
    EfectoEstado = models.CharField(max_length=20 ,choices= StatusBerries , default="Sin Efecto")

         #Metada
    class Meta:
        ordering = ["Nombre"]

    def __str__(self):
        return   self.Nombre
    
    

