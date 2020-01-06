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
        memory = data['memory']
        total_ram = sum(m.size for m in memory)
        motherboard_brands = [brand.name for brand in motherboard.brand.all()]

        if processor.brand.name not in motherboard_brands:
            raise serializers.ValidationError('Processador e placa mãe não são compativeis')

        if not motherboard.integrated_graphics and 'gpu' not in data.keys():
            raise serializers.ValidationError('Placa mãe precisa de uma placa de vídeo!')

        if motherboard.ram_slots < len(memory):
            raise serializers.ValidationError(f'Place mãe só possui {motherboard.ram_slots}')

        if total_ram > motherboard.max_ram:
            raise serializers.ValidationError('A quantidade de ram é maior do que a quantidade máxima da placa mãe')
        return data

    def to_representation(self, instance):
        data = super(OrderSerializer, self).to_representation(instance)
        data['processor'] = ProcessorSerializer(instance.processor).data
        data['memory'] = [MemorySerializer(memory).data for memory in Memory.objects.filter(pk__in=data['memory'])]
        data['gpu'] = GraphicsCardSerializer(instance.gpu).data
        data['motherboard'] = MotherBoardSerializer(instance.motherboard).data
        return data
