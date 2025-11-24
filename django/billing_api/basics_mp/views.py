from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

@api_view(['POST'])
@permission_classes([AllowAny])
def agregar_producto(request):
    try:
        nombre = request.data.get('nombre', '')
        precio = float(request.data.get('precio', 0))
        stock = int(request.data.get('stock', 0))
    except (TypeError, ValueError):
        return Response({"error": "Parametros invalidos"}, status=status.HTTP_400_BAD_REQUEST)
    return Response({
        "nombre": nombre,
        "precio": precio,
        "stock": stock,
        "mensaje": f"Producto {nombre} agregado con éxito"
    })

@api_view(['POST'])
@permission_classes([AllowAny])
def actualizar_stock(request):
    try:
        nombre = request.data.get('nombre', '')
        stock_actual = int(request.data.get('stock_actual', 0))
        stock_nuevo = int(request.data.get('stock_nuevo', 0))
    except (TypeError, ValueError):
        return Response({"error": "Parametros invalidos"}, status=status.HTTP_400_BAD_REQUEST)
    total_stock = stock_actual + stock_nuevo
    return Response({
        "nombre": nombre,
        "stock_actual": stock_actual,
        "stock_nuevo": stock_nuevo,
        "total_stock": total_stock
    })

@api_view(['POST'])
@permission_classes([AllowAny])
def calcular_valor_inventario(request):
    try:
        productos = request.data.get('productos', [])
        # cada producto: {"nombre": str, "precio": float, "cantidad": int}
    except (TypeError, ValueError):
        return Response({"error": "Parametros invalidos"}, status=status.HTTP_400_BAD_REQUEST)
    
    valor_total = 0
    for p in productos:
        try:
            valor_total += float(p.get('precio',0)) * int(p.get('cantidad',0))
        except (TypeError, ValueError):
            return Response({"error": f"Valores invalidos para producto {p.get('nombre','')}"}, status=status.HTTP_400_BAD_REQUEST)
    
    return Response({
        "productos": productos,
        "valor_total_inventario": valor_total
    })

@api_view(['POST'])
@permission_classes([AllowAny])
def productos_por_stock_minimo(request):
    try:
        productos = request.data.get('productos', [])
        minimo = int(request.data.get('minimo',0))
    except (TypeError, ValueError):
        return Response({"error": "Parametros invalidos"}, status=status.HTTP_400_BAD_REQUEST)
    
    filtrados = [p for p in productos if int(p.get('cantidad',0)) < minimo]
    return Response({
        "minimo": minimo,
        "productos_bajo_stock": filtrados
    })

@api_view(['POST'])
@permission_classes([AllowAny])
def promedio_precio_productos(request):
    try:
        productos = request.data.get('productos', [])
        precios = [float(p.get('precio',0)) for p in productos]
    except (TypeError, ValueError):
        return Response({"error": "Parametros invalidos"}, status=status.HTTP_400_BAD_REQUEST)
    
    if len(precios) == 0:
        promedio = 0
    else:
        promedio = sum(precios)/len(precios)
    
    return Response({
        "productos": productos,
        "promedio_precio": promedio
    })

@api_view(['POST'])
@permission_classes([AllowAny])
def valor_producto_con_aumento(request):
    try:
        nombre = request.data.get('nombre','')
        precio = float(request.data.get('precio',0))
        porcentaje = float(request.data.get('porcentaje',0))
    except (TypeError, ValueError):
        return Response({"error": "Parametros invalidos"}, status=status.HTTP_400_BAD_REQUEST)
    
    nuevo_precio = precio + (precio * porcentaje / 100)
    return Response({
        "nombre": nombre,
        "precio_original": precio,
        "porcentaje_aumento": porcentaje,
        "nuevo_precio": nuevo_precio
    })
