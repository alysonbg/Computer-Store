from rest_framework import serializers
from computerstore.computers.models import Order, Processor, Memory, GraphicsCard, MotherBoard


class ProcessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Processor
        fields = ['id','name']


class MemorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Memory
        fields = ['id','name']


class GraphicsCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = GraphicsCard
        fields = ['id','name']


class MotherBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = MotherBoard
        fields = ['id','name']


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['client', 'processor', 'memory', 'gpu', 'motherboard', 'memory']

    def validate(self, data):
        processor = data['processor']
        motherboard = data['motherboard']

        if processor.brand != motherboard.brand:
            raise serializers.ValidationError('Processador e placa mão não são compativeis')

        if not motherboard.integrated_graphics and 'gpu' not in data.keys():
            raise serializers.ValidationError('Placa mãe precisa de uma placa de vídeo!')

        return data
