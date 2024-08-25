from django.urls import path, include   #Usando o framework Django
from rest_framework.routers import DefaultRouter   #Usando o framework DjangoRestFramework DRF

from locadora.views import BrandModelViewSet, CarModelViewSet   #Importando classe do projeto

router = DefaultRouter()   #Usando DRF
router.register('brands', BrandModelViewSet)   #Criando a rota /brands/
router.register('cars', CarModelViewSet)       #Criando a rota /cars/

urlpatterns = [
	path('', include(router.urls)),    #Incluindo as rotas criadas no sistema
]
