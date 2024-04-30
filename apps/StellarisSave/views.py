from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
from apps.StellarisSave.models import Ethic
from apps.StellarisSave.serializers import EthicSerializer

# # Create your views here.

class EthicView(viewsets.ModelViewSet):
    http_method_names = ['get']
    serializer_class = EthicSerializer
    queryset = Ethic.objects.all()

    # def get_queryset(self):
    #     user = self.request.user
    #     return SaveListStellaris.objects.filter(user=user.id)