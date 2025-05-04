# pylint: disable=no-member
"""Vista para el manejo CRUD de empleados."""
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Empleado
from .serializers import EmpleadoSerializer
from .permissions import IsAdminOrAsistenteRRHH, IsLecturaAutorizada
from .permissions import IsEmpleado

class EmpleadoViewSet(viewsets.ModelViewSet):
    """ViewSet que permite listar, crear, editar y eliminar empleados."""
    queryset = Empleado.objects.all()  # pylint: disable=no-member
    serializer_class = EmpleadoSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), IsAdminOrAsistenteRRHH()]
        elif self.action == 'list':
            return [IsAuthenticated(), IsLecturaAutorizada()]
        return super().get_permissions()

class PerfilEmpleadoView(APIView):
    permission_classes = [IsAuthenticated, IsEmpleado]

    def get(self, request):
        try:
            empleado = Empleado.objects.get(usuario=request.user)
        except Empleado.DoesNotExist:
            return Response({"detail": "Empleado no encontrado."}, status=404)

        serializer = EmpleadoSerializer(empleado)
        return Response(serializer.data)
