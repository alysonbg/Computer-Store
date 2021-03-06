# Generated by Django 2.2.8 on 2019-12-15 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computers', '0002_auto_20191214_2303'),
    ]

    operations = [
        migrations.AddField(
            model_name='motherboard',
            name='integrated_graphics',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='motherboard',
            name='max_ram',
            field=models.IntegerField(default=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='motherboard',
            name='ram_slots',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
