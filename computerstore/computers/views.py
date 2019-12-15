from computerstore.computers.models import Order
from computerstore.computers.serializers import OrderSerializer
from rest_framework import generics


class OrderListView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
