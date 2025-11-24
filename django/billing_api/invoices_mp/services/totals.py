from decimal import Decimal, ROUND_HALF_UP
import os

TASA_IMPUESTO = Decimal(os.getenv('TAX_RATE', '0.12'))

def redondear(cantidad):
    return cantidad.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

def calcular_detalle(detalle):
    subtotal = Decimal(detalle.unit_price) * detalle.quantity
    impuesto = redondear(subtotal * TASA_IMPUESTO)
    total = redondear(subtotal + impuesto)
    return redondear(subtotal), impuesto, total

def recalcular_factura(factura):
    from invoices.models import InvoiceDetail
    detalles = InvoiceDetail.objects.filter(invoice=factura)
    subtotal = sum((d.line_subtotal for d in detalles), Decimal('0'))
    impuesto = sum((d.line_tax for d in detalles), Decimal('0'))
    total = sum((d.line_total for d in detalles), Decimal('0'))
    factura.subtotal = redondear(Decimal(subtotal))
    factura.tax = redondear(Decimal(impuesto))
    factura.total = redondear(Decimal(total))
    factura.save(update_fields=['subtotal','tax','total'])
