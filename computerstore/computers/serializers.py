from rest_framework import serializers
from computerstore.computers.models import Order


class OrderSerializer(serializers.ModelSerializer):
    client = serializers.CharField(max_length=100)
    processor = serializers.SlugRelatedField(slug_field='name')
    memory = serializers.SlugRelatedField(slug_field='name', many=True)
    gpu = serializers.SlugRelatedField(slug_field='name')
    motherboard = serializers.SlugRelatedField(slug_field='name')

    class Meta:
        model = Order
        fields = ['client', 'processor', 'memory', 'gpu', 'motherboard']
