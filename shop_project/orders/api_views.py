from rest_framework import generics, viewsets
from drf_spectacular.utils import extend_schema, extend_schema_view

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

@extend_schema_view(
    list=extend_schema(
        summary='Получить все заказы',
        description='Возвращает список всех заказов',
        tags=['Заказы'],
    ),
    create=extend_schema(
        summary='Создать заказ',
        description='Создает новый заказ',
        tags=['Заказы'],
    ),
    retrieve=extend_schema(
        summary='Получить информацию о заказе',
        description='Возвращает детальную информацию о заказе по указанному ID',
        tags=['Заказы'],
    ),
    update=extend_schema(
        summary='Полное обновление заказ',
        description='Обновляет все поля заказа',
        tags=['Заказы'],
    ),
    partial_update=extend_schema(
        summary='Частичное обновление заказа',
        description='Обновляет отдельные поля заказа',
        tags=['Заказы'],
    ),
    destroy=extend_schema(
        summary='Удалить заказ',
        description='Удаляет заказ',
        tags=['Заказы'],
    ),
)
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer