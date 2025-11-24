from rest_framework.routers import DefaultRouter
from invoices.views.invoice import FacturaViewSet
from invoices.views.detail import DetalleFacturaViewSet

router = DefaultRouter()
router.register(r'facturas', FacturaViewSet, basename='factura')
router.register(r'detalles-factura', DetalleFacturaViewSet, basename='detalle-factura')

urlpatterns = router.urls
