from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver
from invoices.models import InvoiceDetail
from invoices.services.totals import compute_detail, recompute_invoice

def actualizar_totales(detalle: InvoiceDetail):
    if not detalle.unit_price:
        detalle.unit_price = detalle.product.price
    subtotal, impuesto, total = compute_detail(detalle)
    detalle.line_subtotal = subtotal
    detalle.line_tax = impuesto
    detalle.line_total = total

@receiver(pre_save, sender=InvoiceDetail)
def antes_guardar_detalle(sender, instance: InvoiceDetail, **kwargs):
    actualizar_totales(instance)

@receiver(post_save, sender=InvoiceDetail)
def despues_guardar_detalle(sender, instance: InvoiceDetail, created, **kwargs):
    recompute_invoice(instance.invoice)

@receiver(post_delete, sender=InvoiceDetail)
def despues_eliminar_detalle(sender, instance: InvoiceDetail, **kwargs):
    recompute_invoice(instance.invoice)
