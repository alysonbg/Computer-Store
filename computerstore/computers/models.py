from django.db import models
from django.core.exceptions import ValidationError

BRANDS = (
    ('INTEL', 'Intel'),
    ('AMD', 'Amd')
)


class Processor(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(choices=BRANDS, max_length=10)


class Memory(models.Model):
    name = models.CharField(max_length=100)
    size = models.IntegerField()


class GraphicsCard(models.Model):
    name = models.CharField(max_length=100)


class MotherBoard(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(choices=BRANDS, max_length=10)
    ram_slots = models.IntegerField()
    max_ram = models.IntegerField()
    integrated_graphics = models.BooleanField()


class Order(models.Model):
    client = models.CharField(max_length=100)
    motherboard = models.ForeignKey('MotherBoard', on_delete=models.CASCADE)
    processor = models.ForeignKey('Processor', on_delete=models.CASCADE)
    memory = models.ForeignKey('Memory', on_delete=models.CASCADE)
    gpu = models.ForeignKey('GraphicsCard', on_delete=models.CASCADE, blank=True, null=True)
