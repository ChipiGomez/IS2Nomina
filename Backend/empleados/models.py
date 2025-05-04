"""Modelo para representar empleados dentro del sistema de nómina."""

from django.db import models
from django.contrib.auth.models import User

class Empleado(models.Model):
    """Contiene los datos personales y salariales del empleado."""
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    cedula = models.CharField(max_length=20, unique=True)
    fecha_ingreso = models.DateField()
    cargo = models.CharField(max_length=50)
    salario_base = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"
