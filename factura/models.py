from django.db import models


class Factura(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    fecha_emision = models.DateField()
    nombre_producto = models.CharField(max_length=100)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def calcular_total(self):
        return self.cantidad * self.precio_unitario

    def __str__(self):
        return (
            f"Factura de {self.nombre_cliente} - valor total: {self.calcular_total()}"
        )
