from django.shortcuts import render
from rest_framework import viewsets

# from apps.user.models import SaveListStellaris
# from apps.user.serializers import SaveListStellarisSerializer


# # Create your views here.

def indexPageView(request):
    return render(request, 'index.html')