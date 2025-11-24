from django.db import models
from catalog.models import Product
from .invoice import Invoice

class DetalleFactura(models.Model):
    factura = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Product, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal_linea = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    impuesto_linea = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total_linea = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return f'{self.producto} x {self.cantidad}'
