import pytest
from django.test import Client
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from factura.models import Factura
from factura.serializer import FacturaSerializer

pytestmark = pytest.mark.django_db


def test_listar_facturas(prueba_factura):
    client = Client()
    url = reverse("listar_facturas")
    response = client.get(url)
    assert response.status_code == 200
    assert "facturas/listar_facturas.html" in [t.name for t in response.templates]
    prueba_factura in response.context_data["facturas"]


def test_crear_factura():
    client = Client()
    url = reverse("nueva_factura")
    data = {
        "nombre_cliente": "Nuevo Cliente",
        "fecha_emision": "2022-01-02",
        "nombre_producto": "Nuevo Producto",
        "cantidad": 2,
        "precio_unitario": 20.0,
    }
    response = client.post(url, data)
    assert response.status_code == 302
    assert response.url == reverse("listar_facturas")
    assert Factura.objects.filter(nombre_cliente="Nuevo Cliente").exists()


def test_editar_factura(prueba_factura):
    client = Client()
    url = reverse("editar_factura", kwargs={"pk": prueba_factura.pk})
    data = {
        "nombre_cliente": "Cliente Modificado",
        "fecha_emision": "2022-01-03",
        "nombre_producto": "Producto Modificado",
        "cantidad": 3,
        "precio_unitario": 30.0,
    }
    response = client.post(url, data)
    assert response.status_code == 302
    assert response.url == reverse("listar_facturas")
    prueba_factura.refresh_from_db()
    assert prueba_factura.nombre_cliente == "Cliente Modificado"
    assert prueba_factura.fecha_emision.strftime("%Y-%m-%d") == "2022-01-03"
    assert prueba_factura.nombre_producto == "Producto Modificado"
    assert prueba_factura.cantidad == 3
    assert prueba_factura.precio_unitario == 30.0


def test_confirmar_eliminar_factura(prueba_factura):
    client = Client()
    url = reverse("eliminar_factura", kwargs={"pk": prueba_factura.pk})
    response = client.get(url)
    assert response.status_code == 200
    assert "facturas/eliminar_factura.html" in [t.name for t in response.templates]
    assert (
        f"¿Estás seguro de que deseas eliminar la factura de {prueba_factura.nombre_cliente}?"
        in response.content.decode("utf-8")
    )


def test_eliminar_factura(prueba_factura):
    client = Client()
    url = reverse("eliminar_factura", kwargs={"pk": prueba_factura.pk})
    response = client.post(url)
    assert response.status_code == 302
    assert response.url == reverse("listar_facturas")
    assert not prueba_factura._meta.model.objects.filter(pk=prueba_factura.pk).exists()


def test_factura_list_create():
    client = APIClient()
    url = reverse("api_listar_facturas")
    data = {
        "nombre_cliente": "Cliente de prueba",
        "fecha_emision": "2022-01-01",
        "nombre_producto": "Producto de prueba",
        "cantidad": 1,
        "precio_unitario": 10.0,
    }
    response = client.post(url, data=data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    assert Factura.objects.filter(nombre_producto=data["nombre_producto"]).exists()
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert (
        FacturaSerializer(
            Factura.objects.get(nombre_producto=data["nombre_producto"])
        ).data
        in response.data
    )
