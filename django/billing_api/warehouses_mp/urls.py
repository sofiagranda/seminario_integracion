from django.urls import path
from . import views

urlpatterns = [
    path('almacenes/lista', views.obtener_lista_almacenes),
    path('almacenes', views.crear_almacen),
    path('almacenes/<int:almacen_id>/', views.obtener_almacen_por_id),
    path('almacenes/<int:almacen_id>/', views.actualizar_almacen),
    path('almacenes/<int:almacen_id>/', views.eliminar_almacen)
]
