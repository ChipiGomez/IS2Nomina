"""Serializador para el modelo Empleado."""

from rest_framework import serializers
from .models import Empleado


class EmpleadoSerializer(serializers.ModelSerializer):
    """Convierte instancias de Empleado en JSON y viceversa."""

    class Meta:
        """Define el modelo y los campos que serán serializados."""
        model = Empleado
        fields = '__all__'
