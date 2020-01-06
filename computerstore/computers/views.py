from computerstore.computers.models import Order, MotherBoard, Memory, GraphicsCard, Processor
from computerstore.computers.serializers import OrderSerializer, MotherBoardSerializer, MemorySerializer, \
     GraphicsCardSerializer, ProcessorSerializer
from rest_framework import viewsets


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class MotherBoardViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MotherBoard.objects.all()
    serializer_class = MotherBoardSerializer


class MemoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Memory.objects.all()
    serializer_class = MemorySerializer


class GraphicsCardViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = GraphicsCard.objects.all()
    serializer_class = GraphicsCardSerializer


class ProcessorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Processor.objects.all()
    serializer_class = ProcessorSerializer
