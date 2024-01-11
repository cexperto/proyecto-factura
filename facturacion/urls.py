from django.contrib import admin
from django.urls import path

from factura.views import (
    CrearFacturaView,
    DetalleFacturaView,
    EditarFacturaView,
    EliminarFacturaView,
    ListarFacturasView,
    inicio,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", inicio, name="inicio"),
    path("facturas/", ListarFacturasView.as_view(), name="listar_facturas"),
    path("facturas/<int:pk>/", DetalleFacturaView.as_view(), name="detalle_factura"),
    path("facturas/nueva/", CrearFacturaView.as_view(), name="nueva_factura"),
    path(
        "facturas/editar/<int:pk>/", EditarFacturaView.as_view(), name="editar_factura"
    ),
    path(
        "facturas/eliminar/<int:pk>/",
        EliminarFacturaView.as_view(),
        name="eliminar_factura",
    ),
]
