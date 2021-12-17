from django.core import paginator
from django.core.exceptions import FieldError
from pokemon_web.models import Pokemon,EntrenadorPK,Maquina_EntrenadorPK,Movimientos,Habilidades,Berries
from .serializers import BerriesSerializer,MaquinaSerializer, PokemonSerializer,EntrenadorPKSerializer,Maquina_EntrenadorPK,MovimientosSerializer,HabilidadesSerializer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.views import APIView, status
from rest_framework.response import Response

# Create your views here.

#////////////////////////////////////////////////////////Entrenador/////////////////////////////////////////////////////////////////

#Entrenador

class EntrenadorView(APIView):
    def get(self, request, format=None):
        if request.method == 'GET':
            data = []
            nextPage = 1
            previousPage = 1
            entrenadores_list = EntrenadorPK.objects.all()
            pagina = request.GET.get('page',1)
            paginador = Paginator(entrenadores_list,5)
            try:
                data = paginador.page(pagina)
            except PageNotAnInteger:
                data = paginador.page(1)
            except EmptyPage:
                data = paginador.page(paginador.num_pages)    
    
            serializer = EntrenadorPKSerializer(data,context = {'request': request}, many= True)
            if data.has_next():
                nextPage = data.next_page_number()
            if data.has_previous():
                previousPage = data.previous_page_number()                

            return Response({'data': serializer.data, 'count': paginador.count})
     
    def post(self,request):
        if request.method == 'POST':
            serializer = EntrenadorPKSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EntrenadorDetail(APIView):
    
    #GET - Saber de un Entrenador Especifico
    
    def get(self,request, ID):
        try:
            entrenador = EntrenadorPK.objects.all(ID=ID)
        except EntrenadorPK.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
         
        if request.method == 'GET':
            serializer = EntrenadorPKSerializer(entrenador, context={'request': request})
            return Response(serializer.data)    
            
#PUT - Edita un Entrenador
    def put(self,request,ID):
        try:
            entrenador = EntrenadorPK.objects.get(ID=ID)
        except EntrenadorPK.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'PUT':
            serializer = EntrenadorPK(entrenador, data=request.data,context={'request':request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#DELETE - Elimina un Entrenador
    def delete(self,request,ID): 
        try:
            entrenador = EntrenadorPK.objects.get(ID = ID)
        except EntrenadorPK.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'DELETE':
            entrenador.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

         
#////////////////////////////////////////////////////////Maquina//////////////////////////////////////////////////////////////////////

class Maquina_EntrenadorPKView(APIView):

# GET - Devuelve todas las maquinas 

    def get(self, request, format=None):
        if request.method == 'GET':
            data = []
            nextPage = 1
            previousPage = 1
            maquinas_list = Maquina_EntrenadorPK.objects.all()
            page = request.GET.get('page',1)
            paginator = Paginator(maquinas_list,5)
            try:
                data = paginator.page(page)
            except PageNotAnInteger:
                data = paginator.page(1)
            except EmptyPage:
                data = paginator.page(paginator.num_pages)
                
            serializer = MaquinaSerializer(data,context={'request': request} ,many=True)
            if data.has_next():
                nextPage = data.next_page_number()
            if data.has_previous():
                previousPage = data.previous_page_number()
                
            return Response( {'data':serializer.data,'count': paginator.count})

# POST - Crea una nueva Maquina 
    def post(self, request):
        if request.method == 'POST':
            serializer = MaquinaSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Maquina_EntrenadorPKDetail(APIView):
#GET - Saber de una Maquina en especifico
    def get(self,request, ID):
        try:
            maquina = Maquina_EntrenadorPK.objects.get(ID=ID)
        except Maquina_EntrenadorPK.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = MaquinaSerializer(maquina, context={'request': request})
            return Response(serializer.data)

#PUT - Edita una Maquina
    def put(self,request,ID):
        try:
            maquina = Maquina_EntrenadorPK.objects.get(ID=ID)
        except Maquina_EntrenadorPK.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'PUT':
            serializer = MaquinaSerializer(maquina, data=request.data,context={'request':request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#DELETE - Elimina una Maquina
    def delete(self,request,ID): 
        try:
            persona = Maquina_EntrenadorPK.objects.get(ID=ID)
        except Maquina_EntrenadorPK.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'DELETE':
            persona.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

#////////////////////////////////////////////////////////Pokemon//////////////////////////////////////////////////////////////////////

class PokemonView(APIView):

# GET - Devuelve todas los pokemons

    def get(self, request, format=None):
        if request.method == 'GET':
            data = []
            nextPage = 1
            previousPage = 1
            pokemons_list = Pokemon.objects.all()
            page = request.GET.get('page',1)
            paginator = Paginator(pokemons_list,5)
            try:
                data = paginator.page(page)
            except PageNotAnInteger:
                data = paginator.page(1)
            except EmptyPage:
                data = paginator.page(paginator.num_pages)
                
            serializer = PokemonSerializer(data,context={'request': request} ,many=True)
            if data.has_next():
                nextPage = data.next_page_number()
            if data.has_previous():
                previousPage = data.previous_page_number()
                
            return Response( {'data':serializer.data,'count': paginator.count})

# POST - Crea un Nuevo Pokemon
    def post(self, request):
        if request.method == 'POST':
            serializer = PokemonSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PokemonDetail(APIView):
#GET - Saber de un Pokemon en especifico
    def get(self,request, ID):
        try:
            pokemon = Pokemon.objects.get(ID=ID)
        except Pokemon.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = PokemonSerializer(pokemon, context={'request': request})
            return Response(serializer.data)

#PUT - Edita un Pokemon
    def put(self,request,ID):
        try:
            pokemon = Pokemon.objects.get(ID=ID)
        except Pokemon.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'PUT':
            serializer = MaquinaSerializer(pokemon, data=request.data,context={'request':request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#DELETE - Elimina un Pokemon
    def delete(self,request,ID): 
        try:
            pokemon = Pokemon.objects.get(ID=ID)
        except Pokemon.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'DELETE':
            pokemon.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

#////////////////////////////////////////////////////////Habilidades//////////////////////////////////////////////////////////////////////

class HabilidadesView(APIView):

# GET - Devuelve todas las habilidades

    def get(self, request, format=None):
        if request.method == 'GET':
            data = []
            nextPage = 1
            previousPage = 1
            habilidades_list = Habilidades.objects.all()
            page = request.GET.get('page',1)
            paginator = Paginator(habilidades_list,5)
            try:
                data = paginator.page(page)
            except PageNotAnInteger:
                data = paginator.page(1)
            except EmptyPage:
                data = paginator.page(paginator.num_pages)
                
            serializer = MaquinaSerializer(data,context={'request': request} ,many=True)
            if data.has_next():
                nextPage = data.next_page_number()
            if data.has_previous():
                previousPage = data.previous_page_number()
                
            return Response( {'data':serializer.data,'count': paginator.count})

# POST - Crea un Nuevo Habilidades
    def post(self, request):
        if request.method == 'POST':
            serializer = HabilidadesSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HabilidadDetail(APIView):
#GET - Saber de una Habilidad en especifico
    def get(self,request, Identificador):
        try:
            habilidad = Habilidades.objects.get(Identificador=Identificador)
        except Habilidades.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = HabilidadesSerializer(habilidad, context={'request': request})
            return Response(serializer.data)

#PUT - Edita una Habilidad
    def put(self,request,Identificador):
        try:
            habilidad = Habilidades.objects.get(Identificador=Identificador)
        except Habilidades.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'PUT':
            serializer = HabilidadesSerializer(habilidad, data=request.data,context={'request':request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#DELETE - Elimina una Habilidad
    def delete(self,request,Identificador): 
        try:
            habilidad = Habilidades.objects.get(Identificador=Identificador)
        except Habilidades.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'DELETE':
            habilidad.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

#////////////////////////////////////////////////////////Movimientos//////////////////////////////////////////////////////////////////////

class MovimientosView(APIView):

# GET - Devuelve todos los movimientos

    def get(self, request, format=None):
        if request.method == 'GET':
            data = []
            nextPage = 1
            previousPage = 1
            movimientos_list = Movimientos.objects.all()
            page = request.GET.get('page',1)
            paginator = Paginator(movimientos_list,5)
            try:
                data = paginator.page(page)
            except PageNotAnInteger:
                data = paginator.page(1)
            except EmptyPage:
                data = paginator.page(paginator.num_pages)
                
            serializer = MovimientosSerializer(data,context={'request': request} ,many=True)
            if data.has_next():
                nextPage = data.next_page_number()
            if data.has_previous():
                previousPage = data.previous_page_number()
                
            return Response( {'data':serializer.data,'count': paginator.count})

# POST - Crea un Nuevo Movimiento
    def post(self, request):
        if request.method == 'POST':
            serializer = MovimientosSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovimientoDetail(APIView):
#GET - Saber de un Movimiento en especifico
    def get(self,request, Identificador_MO):
        try:
            movimiento = Movimientos.objects.get(Identificador_MO=Identificador_MO)
        except Movimientos.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = MovimientosSerializer(movimiento, context={'request': request})
            return Response(serializer.data)

#PUT - Edita un Movimiento
    def put(self,request,Identificador_MO):
        try:
            movimiento = Movimientos.objects.get(Identificador_MO=Identificador_MO)
        except Movimientos.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'PUT':
            serializer = MovimientosSerializer(movimiento, data=request.data,context={'request':request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#DELETE - Elimina un Movimiento

    def delete(self,request,Identificador_MO): 
        try:
            movimiento = Movimientos.objects.get(Identificador_MO=Identificador_MO)
        except Movimientos.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'DELETE':
            movimiento.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

#////////////////////////////////////////////////////////Berries//////////////////////////////////////////////////////////////////


class BerriesView(APIView):

# GET - Devuelve todas las Berries

    def get(self, request, format=None):
        if request.method == 'GET':
            data = []
            nextPage = 1
            previousPage = 1
            berries_list = Berries.objects.all()
            page = request.GET.get('page',1)
            paginator = Paginator(berries_list,5)
            try:
                data = paginator.page(page)
            except PageNotAnInteger:
                data = paginator.page(1)
            except EmptyPage:
                data = paginator.page(paginator.num_pages)
                
            serializer = BerriesSerializer(data,context={'request': request} ,many=True)
            if data.has_next():
                nextPage = data.next_page_number()
            if data.has_previous():
                previousPage = data.previous_page_number()
                
            return Response( {'data':serializer.data,'count': paginator.count})

# POST - Crea una Nueva Berrie
    def post(self, request):
        if request.method == 'POST':
            serializer = BerriesSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BerrieDetail(APIView):
#GET - Saber de una Berrie en especifico
    def get(self,request, Identificador):
        try:
            berrie = Berries.objects.get(Identificador=Identificador)
        except Berries.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = BerriesSerializer(berrie, context={'request': request})
            return Response(serializer.data)

#PUT - Edita una Berrie
    def put(self,request,Identificador):
        try:
            berrie = Berries.objects.get(Identificador=Identificador)
        except Berries.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'PUT':
            serializer = BerriesSerializer(berrie, data=request.data,context={'request':request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#DELETE - Elimina una Berrie

    def delete(self,request,Identificador): 
        try:
            berrie = Berries.objects.get(Identificador=Identificador)
        except Berries.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'DELETE':
            berrie.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

