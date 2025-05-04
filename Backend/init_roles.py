"""Script para crear grupos de roles de usuario en el sistema de nómina."""

from django.contrib.auth.models import Group

roles = ['Administrador', 'Gerente', 'RRHH', 'Asistente RRHH', 'Empleado']

for role in roles:
    group, created = Group.objects.get_or_create(name=role)
    if created:
        print(f"Grupo '{role}' creado.")
    else:
        print(f"Grupo '{role}' ya existe.")
