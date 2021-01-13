from rest_framework import status
from rest_framework.response import Response 
from rest_framework.decorators import api_view

from core.models import Cliente
from core.api.serializers import ClienteSerializer

#GET method
@api_view(['GET', ])
def ApiGETClienteView(request, name):
    try:
        clientes = Cliente.objects.get(name=name)
    except Cliente.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ClienteSerializer(clientes)
        return Response(serializer.data)

#GET method
@api_view(['GET', ])
def ApiLISTClienteView(request):
    clientes = Cliente.objects.all()

    if request.method == 'GET':
        serializer = ClienteSerializer(clientes, many=True)
        return Response(serializer.data)


#PUT method
@api_view(['PATCH', ])
def ApiPUTClienteView(request, name):
    try:
        clientes = Cliente.objects.get(name=name)
    except Cliente.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PATCH':
        serializer = ClienteSerializer(clientes, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["status"] = "success"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#DELETE method
@api_view(['DELETE', ])
def ApiDELETEClienteView(request, name):
    try:
        clientes = Cliente.objects.get(name=name)
    except Cliente.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        operation = clientes.delete()
        data = {}
        if operation:
            data['status'] = "success"
        else:
            data['status'] = 'error'
        return Response(data=data)

#POST method
@api_view(['POST', ])
def ApiPOSTClienteView(request):
    cliente = Cliente()

    if request.method == 'POST':
        serializer = ClienteSerializer(cliente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
