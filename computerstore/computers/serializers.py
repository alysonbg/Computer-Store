from rest_framework import serializers
from computerstore.computers.models import Order, Processor, Memory, GraphicsCard, MotherBoard


class ProcessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Processor
        fields = ['name', 'brand']


class MemorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Memory
        fields = ['name', 'size']


class GraphicsCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = GraphicsCard
        fields = ['name']


class MotherBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = MotherBoard
        fields = ['name', 'brand', 'ram_slots', 'max_ram', 'integrated_graphics']


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['id', 'client', 'processor', 'memory', 'gpu', 'motherboard']

    def validate(self, data):
        processor = data['processor']
        motherboard = data['motherboard']

        if processor.brand != motherboard.brand:
            raise serializers.ValidationError('Processador e placa mão não são compativeis')

        if not motherboard.integrated_graphics and 'gpu' not in data.keys():
            raise serializers.ValidationError('Placa mãe precisa de uma placa de vídeo!')

        return data

    def to_representation(self, instance):
        data = super(OrderSerializer, self).to_representation(instance)
        data['processor'] = ProcessorSerializer(instance.processor).data
        data['memory'] = [MemorySerializer(memory).data for memory in Memory.objects.filter(pk__in=data['memory'])]
        data['gpu'] = GraphicsCardSerializer(instance.gpu).data
        data['motherboard'] = MotherBoardSerializer(instance.motherboard).data
        return data
