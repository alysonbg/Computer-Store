# Generated by Django 2.2.8 on 2020-01-06 01:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('computers', '0006_auto_20200106_0113'),
    ]
    def insert_defaut_data(apps, schema_editor):
        Brand = apps.get_model('computers', 'Brand')
        intel = Brand.objects.create(name='INTEL')
        amd = Brand.objects.create(name='AMD')

        Processor = apps.get_model('computers', 'Processor')
        Processor.objects.create(name='Processador Intel Core i5', brand=intel)
        Processor.objects.create(name='Processador Intel Core i7', brand=intel)
        Processor.objects.create(name='Processador AMD Athlon', brand=amd)
        Processor.objects.create(name='Processador AMD Ryzen 7', brand=amd)

        Motherboard = apps.get_model('computers', 'Motherboard')
        asus = Motherboard.objects.create(name='Placa Mãe AsusPrime', ram_slots=2, max_ram=16, integrated_graphics=False)
        asus.brand.add(intel)
        gygabyte = Motherboard.objects.create(name='Placa Mãe Gigabyte', ram_slots=2, max_ram=16, integrated_graphics=False)
        gygabyte.brand.add(amd)
        asrock = Motherboard.objects.create(name='Placa Mãe ASRock Fatal', ram_slots=4, max_ram=32, integrated_graphics=True)
        asrock.brand.add(intel)
        asrock.brand.add(amd)

        Graphicscard = apps.get_model('computers', 'GraphicsCard')
        Graphicscard.objects.create(name='Placa de Video Gigabyte Geforce GTX 1060 6GB')
        Graphicscard.objects.create(name='Placa de Video PNY RTX 2060 6GB')      
        Graphicscard.objects.create(name='Placa de Video Radeon RX 580 8GB')

        Memory = apps.get_model('computers', 'Memory')
        Memory.objects.create(name='Hiper X 4gb', size=4)      
        Memory.objects.create(name='Hiper X 8gb', size=8)      
        Memory.objects.create(name='Hiper X 16gb', size=16)      
        Memory.objects.create(name='Hiper X 32gb', size=32)      
        Memory.objects.create(name='Hiper X 64gb', size=64)

    operations = [
        migrations.RunPython(insert_defaut_data),
    ]


