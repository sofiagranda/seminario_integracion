from rest_framework import viewsets, filters
from catalog.models import Product
from catalog.serializers import ProductSerializer
from catalog.permissions import IsAdminOrReadOnly
from catalog.pagination import StandardResultsSetPagination

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.select_related("category").all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = StandardResultsSetPagination
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ("nombre", "slug", "category__nombre")
    ordering_fields = ("precio", "creado_en", "nombre")

    def get_queryset(self):
        qs = super().get_queryset()
        categoria = self.request.query_params.get("categoria")
        esta_activo = self.request.query_params.get("esta_activo")
        if categoria:
            qs = qs.filter(category__id=categoria)
        if esta_activo is not None:
            qs = qs.filter(is_active=esta_activo.lower() in ("1","true","t","yes"))
        return qs
