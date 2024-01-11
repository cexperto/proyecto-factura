from django import forms

from factura.models import Factura


class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = [
            "nombre_cliente",
            "fecha_emision",
            "nombre_producto",
            "cantidad",
            "precio_unitario",
        ]
