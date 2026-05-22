from rest_framework import generics, viewsets
from drf_spectacular.utils import extend_schema, extend_schema_view

from .models import Review
from .serializers import ReviewSerializer

@extend_schema(
    summary='Список отзывов',
    description='Возвращает список всех отзывов ко всем товарам',
    tags=['Отзывы'],
)
class ReviewListAPIView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

@extend_schema(
    summary='Детальная информация об отзыве',
    description='Возвращает один отзыв по его ID',
    tags=['Отзывы'],
)
class ReviewDetailAPIView(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

@extend_schema_view(
    list=extend_schema(
        summary='Получить отзывы',
        description='Возвращает все отзывы',
        tags=['Отзывы'],
    ),
    create=extend_schema(
        summary='Создать новый отзыв',
        description='Создает новый отзыв',
        tags=['Отзывы'],
    ),
    retrieve=extend_schema(
        summary='Получить информацию об отзыве',
        description='Возвращает детальную информацию об отзыве по его ID.',
        tags=['Отзывы'],
    ),
    update=extend_schema(
        summary='Полное обновление отзыва',
        description='Обновляет все поля отзыва',
        tags=['Отзывы'],
    ),
    partial_update=extend_schema(
        summary='Частичное обновление отзыва',
        description='Обновляет отдельные поля отзыва',
        tags=['Отзывы'],
    ),
    destroy=extend_schema(
        summary='Удалить отзыв',
        description='Удаляет отзыв',
        tags=['Отзывы'],
    ),
)
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer