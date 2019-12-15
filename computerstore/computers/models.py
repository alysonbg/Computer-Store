from django.db import models

BRANDS = (
    ('INTEL', 'Intel'),
    ('AMD', 'Amd')
)


class Processor(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(choices=BRANDS, max_length=10)

    def __str__(self):
        return self.name


class Memory(models.Model):
    name = models.CharField(max_length=100)
    size = models.IntegerField()

    def __str__(self):
        return '{} {}GB'.format(self.name, self.size)


class GraphicsCard(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class MotherBoard(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(choices=BRANDS, max_length=10)
    ram_slots = models.IntegerField()
    max_ram = models.IntegerField()
    integrated_graphics = models.BooleanField()

    def __str__(self):
        return self.name


class Order(models.Model):
    client = models.CharField(max_length=100)
    motherboard = models.ForeignKey('MotherBoard', on_delete=models.CASCADE)
    processor = models.ForeignKey('Processor', on_delete=models.CASCADE)
    memory = models.ManyToManyField('Memory')
    gpu = models.ForeignKey('GraphicsCard', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return '{} - {}'.format(self.client, self.id)
