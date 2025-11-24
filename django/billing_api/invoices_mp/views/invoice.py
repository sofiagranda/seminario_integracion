from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db import transaction
from django.utils.crypto import get_random_string
from invoices.models import Invoice
from invoices.serializers.invoice import InvoiceSerializer, InvoiceCreateSerializer
from invoices.serializers.detail import InvoiceDetailSerializer
from invoices.services.totals import recompute_invoice
from catalog.models import Product

class EsPropietarioOAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj.user_id == request.user.id

class FacturaViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ('status',)
    search_fields = ('customer_name', 'customer_email', 'number')
    ordering_fields = ('created_at', 'total')

    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.request.user.is_staff:
            queryset = queryset.filter(user=self.request.user)
        return queryset

    def get_serializer_class(self):
        if self.action in ('create', 'update', 'partial_update'):
            return InvoiceCreateSerializer
        return InvoiceSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'])
    def agregar_item(self, request, pk=None):
        factura = self.get_object()
        self.check_object_permissions(request, factura)
        if factura.status != Invoice.DRAFT:
            return Response({'detalle': 'Solo puedes agregar items en borrador'}, status=400)

        serializer = InvoiceDetailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(invoice=factura)
        recompute_invoice(factura)
        return Response(InvoiceSerializer(factura).data)

    @action(detail=True, methods=['post'])
    @transaction.atomic
    def finalizar(self, request, pk=None):
        factura = self.get_object()
        self.check_object_permissions(request, factura)
        if factura.status != Invoice.DRAFT:
            return Response({'detalle': 'La factura no está en borrador'}, status=400)

        if not factura.number:
            factura.number = f'INV-{get_random_string(6).upper()}'

        for detalle in factura.details.select_related('product'):
            producto: Product = detalle.product
            if producto.stock < detalle.quantity:
                return Response({'detalle': f'Sin stock para {producto.name}'}, status=400)

        for detalle in factura.details.select_related('product'):
            producto: Product = detalle.product
            producto.stock -= detalle.quantity
            producto.save(update_fields=['stock'])

        factura.status = Invoice.FINALIZED
        factura.save(update_fields=['number','status'])
        recompute_invoice(factura)
        return Response(InvoiceSerializer(factura).data, status=200)

    @action(detail=True, methods=['post'])
    @transaction.atomic
    def cancelar(self, request, pk=None):
        factura = self.get_object()
        self.check_object_permissions(request, factura)
        if factura.status == Invoice.CANCELED:
            return Response({'detalle':'La factura ya está cancelada'}, status=400)

        if factura.status == Invoice.FINALIZED:
            for detalle in factura.details.select_related('product'):
                producto: Product = detalle.product
                producto.stock += detalle.quantity
                producto.save(update_fields=['stock'])

        factura.status = Invoice.CANCELED
        factura.save(update_fields=['status'])
        recompute_invoice(factura)
        return Response(InvoiceSerializer(factura).data, status=200)
