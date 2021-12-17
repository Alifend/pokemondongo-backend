from django.urls import path
from .views import EntrenadorView,EntrenadorDetail, HabilidadDetail, HabilidadesView,Maquina_EntrenadorPKView
from .views import MovimientoDetail, MovimientosView, PokemonDetail, PokemonView,Maquina_EntrenadorPKDetail
from .views import BerrieDetail,BerriesView

urlpatterns = [

path('entrenador/', EntrenadorView.as_view()),
path('entrenador/<str:ID>',EntrenadorDetail.as_view()),

path('maquina/', Maquina_EntrenadorPKView.as_view()),
path('maquina/<str:ID>',Maquina_EntrenadorPKDetail.as_view()),

path('pokemon/', PokemonView.as_view()),
path('pokemon/<str:ID>',PokemonDetail.as_view()),

path('habilidad/', HabilidadesView.as_view()),
path('habilidad/<str:Identificador>',HabilidadDetail.as_view()),

path('movimientos/',MovimientosView.as_view()),
path('movimientos/<str:Identificador_MO>',MovimientoDetail.as_view()),

path('berries/', BerriesView.as_view()),
path('berries/<str:Identificador>',BerrieDetail.as_view())

]