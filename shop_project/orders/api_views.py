from rest_framework import generics
from drf_spectacular.utils import extend_schema

from .models import Order
from .serializers import OrderSerializer

@extend_schema(
    summary='Список заказов',
    description='Возвращает список всех заказов с товарами и статусом оплаты',
    tags=['Заказы'],
)
class OrderListAPIView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

@extend_schema(
    summary='Детальная информация о заказе',
    description='Возвращает один заказ по его ID, включая вложенные позиции (товары)',
    tags=['Заказы'],
)
class OrderDetailAPIView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer