from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Processor, Memory, MotherBoard, GraphicsCard


class ApiTesting(APITestCase):
    def setUp(self):
        self.processor_intel = Processor.objects.create(name='Processador Intel Core i7', brand='INTEL')
        self.processor_amd = Processor.objects.create(name='Processador AMD Athlon', brand='AMD')
        self.mother_board = MotherBoard.objects.create(
            name='Placa Mãe AsusPrime',
            brand='INTEL',
            ram_slots=2,
            max_ram=16,
            integrated_graphics=False
        )
        self.memory_4gb = Memory.objects.create(name='Hyper X', size=4)
        self.memory_16gb = Memory.objects.create(name='Hyper X', size=16)
        self.gpu = GraphicsCard.objects.create(name='Placa de Video Gigabyte Geforce GTX 1060 6GB')

    def test_create_a_new_order(self):
        """Testa se é possível criar um novo pedido quando todos os dados sao validos"""
        url = reverse('orders')
        data = {
            'client': 'Test99',
            'processor': self.processor_intel.id,
            'motherboard': self.mother_board.id,
            'memory': [self.memory_4gb.id],
            'gpu': self.gpu.id,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_motherboard_and_processor_validation(self):
        """Testa a compatilidade entre placa mae e processador"""
        url = reverse('orders')
        data = {
            'client': 'Test99',
            'processor': self.processor_amd.id,
            'motherboard': self.mother_board.id,
            'memory': [self.memory_4gb.id],
            'gpu': self.gpu.id,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_graphicscard_motherboard_validation(self):
        """Testa se nao e possivel criar uma ordem tem gpu, caso a placa mae nao tenha video integrado"""
        url = reverse('orders')
        data = {
            'client': 'Test99',
            'processor': self.processor_intel.id,
            'motherboard': self.mother_board.id,
            'memory': [self.memory_4gb.id]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_if_is_not_possible_to_create_an_order_that_exceeds_memory_slots(self):
        """Testa se nao e possivel criar uma ordem que exceda o numero de slots da placa mae"""
        url = reverse('orders')
        data = {
            'client': 'Test99',
            'processor': self.processor_intel.id,
            'motherboard': self.mother_board.id,
            'memory': [self.memory_4gb.id for _ in range(3)],
            'gpu': self.gpu.id,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_if_is_not_possible_to_create_an_order_that_exceeds_max_memory(self):
        """Testa se nao e possivel criar uma ordem que exceda a quantidade maxima de ram da placa mae"""
        url = reverse('orders')
        data = {
            'client': 'Test99',
            'processor': self.processor_intel.id,
            'motherboard': self.mother_board.id,
            'memory': [self.memory_16gb.id for _ in range(2)],
            'gpu': self.gpu.id,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
