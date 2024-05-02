from rest_framework import serializers

from apps.StellarisSave.models import *


class EthicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ethic
        fields = ['name', 'description', 'effect', 'cost', 'image']


class PlanetTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanetType
        fields = ['id', 'name', 'description']


class PlanetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planet
        fields = ['id', 'name', 'description', 'image', 'type']


class BackgroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Background
        fields = ['id', 'image']


class FlagTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlagType
        fields = ['id', 'name']


class FlagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flag
        fields = ['id', 'image', 'type']


class RaceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RaceType
        fields = ['id', 'name']


class RaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        fields = ['id', 'name', 'image', 'type']


class ShipTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShipType
        fields = ['id', 'image']


class OriginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Origin
        fields = ['id', 'name', 'description', 'effect', 'requirement', 'image']


class GovernmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Government
        fields = ['id', 'name', 'description', 'effect', 'requirement', 'image']


class CivicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civic
        fields = ['id', 'name', 'description', 'effect', 'requirement', 'image']


class GeneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gene
        fields = ['id', 'name', 'description', 'effect', 'requirement', 'cost', 'image']


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['id', 'color']
