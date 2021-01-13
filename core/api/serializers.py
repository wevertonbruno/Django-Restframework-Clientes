from rest_framework import serializers
from core.models import Cliente

# Serializers define the API representation.
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['name', 'age', 'gender']