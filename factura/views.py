from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from rest_framework.generics import ListCreateAPIView

from factura.forms import FacturaForm
from factura.models import Factura
from factura.serializer import FacturaSerializer


def inicio(request):
    """Vista que indica la pagina de inicio"""
    return HttpResponse("inicio")


class ListarFacturasView(ListView):
    """Vista de lista para visuaizar todas las facturas registradas"""

    model = Factura
    template_name = "facturas/listar_facturas.html"
    context_object_name = "facturas"


class DetalleFacturaView(DetailView):
    """Vista para visuaizar el detalle de una factura"""

    model = Factura
    template_name = "facturas/detalle_factura.html"
    context_object_name = "factura"


class CrearFacturaView(CreateView):
    """Vista para hacer la creacion de un registro de factura"""

    model = Factura
    form_class = FacturaForm
    template_name = "facturas/editar_factura.html"
    success_url = reverse_lazy("listar_facturas")


class EditarFacturaView(UpdateView):
    """Vista para hacer la actualizacion de un registro de factura"""

    model = Factura
    form_class = FacturaForm
    template_name = "facturas/editar_factura.html"
    success_url = reverse_lazy("listar_facturas")


class EliminarFacturaView(DeleteView):
    """Vista para eliminar un registro de factura"""

    model = Factura
    template_name = "facturas/eliminar_factura.html"
    success_url = reverse_lazy("listar_facturas")


class FacturaListCreateAPIView(ListCreateAPIView):
    """Endpoint para listar y crear facturas"""

    permission_classes = []
    serializer_class = FacturaSerializer
    queryset = Factura.objects.all()
