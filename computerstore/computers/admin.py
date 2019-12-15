from django.contrib import admin
from computerstore.computers.models import Order, MotherBoard, Processor, Memory, GraphicsCard


admin.site.register(Order)
admin.site.register(MotherBoard)
admin.site.register(Processor)
admin.site.register(Memory)
admin.site.register(GraphicsCard)
