from rest_framework import serializers
from invoices.models import InvoiceDetail
from catalog.models import Product

class DetalleFacturaSerializer(serializers.ModelSerializer):
    producto_id = serializers.PrimaryKeyRelatedField(
        source='product', queryset=Product.objects.all(), write_only=True
    )
    nombre_producto = serializers.ReadOnlyField(source='product.name')

    class Meta:
        model = InvoiceDetail
        fields = ('id','invoice','producto_id','nombre_producto','quantity','unit_price',
                  'line_subtotal','line_tax','line_total')
        read_only_fields = ('id','line_subtotal','line_tax','line_total','nombre_producto')
