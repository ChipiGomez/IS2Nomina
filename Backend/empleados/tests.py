from django.contrib.auth.models import User, Group
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import Empleado

class EmpleadoTests(APITestCase):
    def setUp(self):
        # Crear grupo y usuario con rol Administrador
        self.admin_group, _ = Group.objects.get_or_create(name='Administrador')
        self.admin_user = User.objects.create_user(username='admin_test', password='test1234')
        self.admin_user.groups.add(self.admin_group)

        # Obtener token JWT
        response = self.client.post('/api/token/', {'username': 'admin_test', 'password': 'test1234'})
        self.token = response.data['access']

        # Configurar cliente autenticado
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

    def test_crear_empleado(self):
        data = {
            "nombres": "Juan",
            "apellidos": "Pérez",
            "cedula": "1234567",
            "fecha_ingreso": "2024-01-10",
            "cargo": "Analista",
            "salario_base": "3500000.00"
        }
        response = self.client.post('/api/empleados/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_permiso_restringido_a_no_admin(self):
        # Usuario sin grupo
        user = User.objects.create_user(username='empleado_test', password='test1234')
        response = self.client.post('/api/token/', {'username': 'empleado_test', 'password': 'test1234'})
        token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        response = self.client.get('/api/empleados/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
