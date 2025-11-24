from django.urls import path
from . import views
urlpatterns = [
    path('area-triangulo/', views.area_triangulo),
    path('tabla-multiplicar/', views.tabla_multiplicar),
    path('contar-mayores/', views.contar_mayores),
    path('suma-consecutivos/', views.suma_consecutivos),
    path('promedio/', views.promedio),
    path('potencia/', views.potencia),
]