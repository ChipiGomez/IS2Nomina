"""Configuración de la aplicación Empleados."""

from django.apps import AppConfig


class EmpleadosConfig(AppConfig):
    """Configuración para la app 'empleados'."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'empleados'
