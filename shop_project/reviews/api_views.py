from rest_framework import generics
from drf_spectacular.utils import extend_schema

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