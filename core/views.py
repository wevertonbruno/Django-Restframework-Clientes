from django.shortcuts import render
from rest_framework import viewsets
from .models import Cliente
from .serializers import ClienteSerializer

# ViewSets define the view behavior.
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

""" class ClienteGenderViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.filter(gender="Male")
    serializer_class = ClienteGenderSerializer """
