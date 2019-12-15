from rest_framework import serializers
from computerstore.computers.models import Order, Processor, Memory, GraphicsCard, MotherBoard


class ProcessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Processor
        fields = ['name']


class MemorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Memory
        fields = ['name']


class GraphicsCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = GraphicsCard
        fields = ['name']


class MotherBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = MotherBoard
        fields = ['name']


class OrderSerializer(serializers.ModelSerializer):
    client = serializers.CharField(max_length=100)
    processor = serializers.SlugRelatedField(slug_field='name', queryset=Processor.objects.all())
    memory = serializers.SlugRelatedField(slug_field='name', queryset=Memory.objects.all(), many=True)
    gpu = serializers.SlugRelatedField(slug_field='name', queryset=GraphicsCard.objects.all())
    motherboard = serializers.SlugRelatedField(slug_field='name', queryset=MotherBoard.objects.all())

    class Meta:
        model = Order
        fields = ['client', 'processor', 'memory', 'gpu', 'motherboard']

    def validate(self, data):
        data = self.get_initial()
        processor_data = data['processor']
        motherboard_data = data['motherboard']
        processor = Processor.objects.get(name__exact=processor_data)
        motherboard = MotherBoard.objects.get(name__exact=motherboard_data)

        if processor.brand != motherboard.brand:
            raise serializers.ValidationError("Processador e placa mão não são compativeis")
