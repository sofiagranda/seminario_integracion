from rest_framework import viewsets, permissions
from rest_framework.exceptions import PermissionDenied, ValidationError
from invoices.models import InvoiceDetail
from invoices.serializers.detail import InvoiceDetailSerializer
from invoices.services import totals

class InventarioDetalleViewSet(viewsets.ModelViewSet):
    serializer_class = InvoiceDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = InvoiceDetail.objects.select_related('invoice', 'product')
        if not self.request.user.is_staff:
            queryset = queryset.filter(invoice__user=self.request.user)
        return queryset

    def perform_create(self, serializer):
        factura = serializer.validated_data['invoice']

        if not self.request.user.is_staff and factura.user != self.request.user:
            raise PermissionDenied('No puedes modificar facturas de otros usuarios')

        if factura.status != factura.DRAFT:
            raise ValidationError('Solo puedes agregar detalles cuando la factura está en Borrador')

        serializer.save()
        totals.recalcular_factura(factura)
