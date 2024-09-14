from rest_framework import viewsets, permissions
from locadora.models import Brand, Car
from locadora.serializers import BrandModelSerializer, CarModelSerializer
from dj_rql.drf import RQLFilterBackend
from locadora.filters import BrandFilterClass, CarFilterClass
from locadora.permissions import LocadoraOwnerPermission


class BrandModelViewSet(viewsets.ModelViewSet):
	queryset = Brand.objects.all()
	serializer_class = BrandModelSerializer
	filter_backends = [RQLFilterBackend]   # Permite utilizar loockups pré-determinados na requisição GET
	rql_filter_class = BrandFilterClass    # Informa qual rota/classe vai pode utilizar as rql's


class CarModelViewSet(viewsets.ModelViewSet):
	queryset = Car.objects.all()
	serializer_class = CarModelSerializer
	filter_backends = [RQLFilterBackend]
	rql_filter_class = CarFilterClass
	permission_classes = [permissions.DjangoModelPermissions, LocadoraOwnerPermission,]
