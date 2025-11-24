from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..models import Almacen
from ..serializers import AlmacenSerializer

@api_view(["GET"])
def obtener_lista_almacenes(request):
    qs = Almacen.objects.all()
    q = (request.query_params.get("q") or "").strip()
    if q:
        qs = qs.filter(Q(codigo__icontains=q) |
                       Q(nombre__icontains=q) |
                       Q(ciudad__icontains=q))
    data = AlmacenSerializer(qs, many=True).data
    return Response(data, status=status.HTTP_200_OK)

@api_view(["POST"])
def crear_almacen(request):
    serializer = AlmacenSerializer(data=request.data)
    if serializer.is_valid():
        almacen = serializer.save()
        return Response(AlmacenSerializer(almacen).data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET"])
def obtener_almacen_por_id(request, almacen_id: int):
    try:
        almacen = Almacen.objects.get(pk=almacen_id)
    except Almacen.DoesNotExist:
        return Response({'Detalle': 'No encontrado'}, status=status.HTTP_404_NOT_FOUND)
    
    return Response(AlmacenSerializer(almacen).data, status=status.HTTP_200_OK)

@api_view(["PUT"])
def actualizar_almacen(request, almacen_id: int):
    try:
        almacen = Almacen.objects.get(pk=almacen_id)
    except Almacen.DoesNotExist:
        return Response({'Detalle': 'No encontrado'}, status=status.HTTP_404_NOT_FOUND)
    serializer = AlmacenSerializer(almacen, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def eliminar_almacen(request, almacen_id: int):
    try:
        almacen = Almacen.objects.get(pk=almacen_id)
    except Almacen.DoesNotExist:
        return Response({'Detalle': 'No encontrado'}, status=status.HTTP_404_NOT_FOUND)
    almacen.delete()
    return Response({'Detalle': 'Registro eliminado'}, status=status.HTTP_200_OK)
