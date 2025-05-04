"""Permisos personalizados para controlar el acceso según grupos de usuario."""

from rest_framework.permissions import BasePermission

class IsAdministrador(BasePermission):
    """Permite acceso solo a usuarios en el grupo 'Administrador'."""
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='Administrador').exists()


class IsGerente(BasePermission):
    """Permite acceso solo a usuarios en el grupo 'Gerente'."""
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='Gerente').exists()


class IsRRHH(BasePermission):
    """Permite acceso solo a usuarios en el grupo 'RRHH'."""
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='RRHH').exists()


class IsAsistenteRRHH(BasePermission):
    """Permite acceso solo a usuarios en el grupo 'Asistente RRHH'."""
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='Asistente RRHH').exists()


class IsEmpleado(BasePermission):
    """Permite acceso solo a usuarios en el grupo 'Empleado'."""
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='Empleado').exists()


# ------------------------------------------------------------------
# Permisos combinados para acciones específicas (autorización múltiple)
# ------------------------------------------------------------------

class IsInGroups(BasePermission):
    """Clase base que permite acceso si el usuario pertenece a uno o más grupos especificados."""
    def __init__(self, groups):
        self.groups = groups

    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name__in=self.groups).exists()


class IsAdminOrAsistenteRRHH(IsInGroups):
    """Permite acceso a Administrador o Asistente RRHH."""
    def __init__(self):
        super().__init__(groups=['Administrador', 'Asistente RRHH'])


class IsLecturaAutorizada(IsInGroups):
    """Permite acceso a todos los roles con permiso de lectura (Administrador, Gerente, 
    RRHH, Asistente RRHH)."""
    def __init__(self):
        super().__init__(groups=['Administrador', 'Asistente RRHH', 'RRHH', 'Gerente'])
