from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
from apps.StellarisSave.serializers import *


# # Create your views here.

class EthicView(viewsets.ModelViewSet):
    http_method_names = ['get']
    serializer_class = EthicSerializer
    queryset = Ethic.objects.all()


class PlanetTypeView(viewsets.ModelViewSet):
    http_method_names = ['get']
    serializer_class = PlanetTypeSerializer
    queryset = PlanetType.objects.all()


class PlanetView(viewsets.ModelViewSet):
    http_method_names = ['get']
    serializer_class = PlanetSerializer
    queryset = Planet.objects.all()


class BackgroundView(viewsets.ModelViewSet):
    http_method_names = ['get']
    serializer_class = Background
    queryset = Background.objects.all()


class FlagTypeView(viewsets.ModelViewSet):
    http_method_names = ['get']
    serializer_class = FlagTypeSerializer
    queryset = FlagType.objects.all()


class FlagView(viewsets.ModelViewSet):
    http_method_names = ['get']
    serializer_class = FlagSerializer
    queryset = Flag.objects.all()


class RaceTypeView(viewsets.ModelViewSet):
    http_method_names = ['get']
    serializer_class = RaceTypeSerializer
    queryset = RaceType.objects.all()


class RaceView(viewsets.ModelViewSet):
    http_method_names = ['get']
    serializer_class = RaceSerializer
    queryset = Race.objects.all()


class ShipTypeView(viewsets.ModelViewSet):
    http_method_names = ['get']
    serializer_class = ShipTypeSerializer
    queryset = ShipType.objects.all()


class OriginView(viewsets.ModelViewSet):
    http_method_names = ['get']
    serializer_class = OriginSerializer
    queryset = Origin.objects.all()


class GovernmentView(viewsets.ModelViewSet):
    http_method_names = ['get']
    serializer_class = GovernmentSerializer
    queryset = Government.objects.all()


class CivicView(viewsets.ModelViewSet):
    http_method_names = ['get']
    serializer_class = CivicSerializer
    queryset = Civic.objects.all()


class GeneView(viewsets.ModelViewSet):
    http_method_names = ['get']
    serializer_class = GeneSerializer
    queryset = Gene.objects.all()


class ColorView(viewsets.ModelViewSet):
    http_method_names = ['get']
    serializer_class = ColorSerializer
    queryset = Color.objects.all()
