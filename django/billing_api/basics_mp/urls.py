from django.urls import path
from . import views

urlpatterns = [
    path('agregar-producto/', views.agregar_producto),
    path('actualizar-stock/', views.actualizar_stock),
    path('calcular-valor-inventario/', views.calcular_valor_inventario),
    path('productos-por-stock-minimo/', views.productos_por_stock_minimo),
    path('promedio-precio-productos/', views.promedio_precio_productos),
    path('valor-producto-con-aumento/', views.valor_producto_con_aumento),
]
