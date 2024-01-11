import pytest

from factura.models import Factura


@pytest.fixture
def prueba_factura(db):
    return Factura.objects.create(
        nombre_cliente="Cliente Test",
        fecha_emision="2022-01-01",
        nombre_producto="Producto Test",
        cantidad=1,
        precio_unitario=10.0,
    )
