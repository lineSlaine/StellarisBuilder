from django.shortcuts import render
from rest_framework import viewsets

# from apps.user.models import SaveListStellaris
# from apps.user.serializers import SaveListStellarisSerializer


# # Create your views here.

# class UserStellarisSaveListApiView(viewsets.ModelViewSet):

#     serializer_class = SaveListStellarisSerializer
#     queryset = SaveListStellaris.objects.all()
    # def get_queryset(self):
    #     user = self.request.user
    #     return SaveListStellaris.objects.filter(user=user.id)
