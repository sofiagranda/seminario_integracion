from rest_framework import viewsets, filters
from catalog.models import CategoriaInventario
from catalog.serializers import CategoriaInventarioSerializer
from catalog.permissions import IsAdminOrReadOnly

class CategoriaInventarioViewSet(viewsets.ModelViewSet):
    queryset = CategoriaInventario.objects.all()
    serializer_class = CategoriaInventarioSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ("nombre", "slug")
    ordering_fields = ("nombre", "creado_en")
