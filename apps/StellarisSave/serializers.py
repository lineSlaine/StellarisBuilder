from rest_framework import serializers

from apps.StellarisSave.models import *


class EthicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ethic
        fields = ['name', 'image', 'description', 'effect', 'cost']
