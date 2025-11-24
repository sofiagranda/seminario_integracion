from rest_framework import serializers
from invoices.models import Invoice, InvoiceDetail
from invoices.serializers.detail import DetalleFacturaSerializer

class FacturaSerializer(serializers.ModelSerializer):
    detalles = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Invoice
        fields = ('id','number','customer_name','customer_email','status',
                  'subtotal','tax','total','created_at','updated_at','detalles')
        read_only_fields = ('id','number','subtotal','tax','total','created_at','updated_at','detalles')

    def get_detalles(self, obj):
        qs = InvoiceDetail.objects.filter(invoice=obj).select_related('product')
        return DetalleFacturaSerializer(qs, many=True).data

class FacturaCrearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ('customer_name','customer_email')
