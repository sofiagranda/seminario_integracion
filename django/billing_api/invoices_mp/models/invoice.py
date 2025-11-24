from django.db import models
from django.contrib.auth.models import User

class Factura(models.Model):
    BORRADOR = 'BORRADOR'
    FINALIZADA = 'FINALIZADA'
    CANCELADA = 'CANCELADA'
    OPCIONES_ESTADO = [
        (BORRADOR, 'Borrador'),
        (FINALIZADA, 'Finalizada'),
        (CANCELADA, 'Cancelada'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='facturas')
    numero = models.CharField(max_length=32, unique=True, blank=True)
    nombre_cliente = models.CharField(max_length=160)
    email_cliente = models.EmailField(blank=True)
    estado = models.CharField(max_length=16, choices=OPCIONES_ESTADO, default=BORRADOR)

    subtotal = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    impuesto = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-creado_en',)

    def __str__(self):
        return f'Factura #{self.id} - {self.nombre_cliente}'
