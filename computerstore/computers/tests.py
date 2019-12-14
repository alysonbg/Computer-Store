from django.test import TestCase
from .models import MotherBoard, Processor
from .models import BRANDS


class MotherBoardTestCase(TestCase):
    def setUp(self):
        self.processor_amd = Processor.objects.create(name='Ryzen 5', brand=BRANDS[0])
        self.processor_intel = Processor.objects.create(name='I7', brand=BRANDS[1])

    def test_if_mother_board_and_processors_are_from_the_same_brand(self):
        """It tests if is possible to create a new motherboard using a processor that is supported"""
        motherboard = MotherBoard(name='Gybabyte', brand=BRANDS[0], processor=self.processor_amd)
        self.assertEqual(motherboard.brand, self.processor_amd.brand)
