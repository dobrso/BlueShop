from rest_framework import generics
from drf_spectacular.utils import extend_schema

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

@extend_schema(
    summary='Список категорий',
    description='Возвращает массив всех доступных категорий товаров',
    tags=['Категории'],
)
class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

@extend_schema(
    summary='Список товаров',
    description='Возвращает массив всех товаров',
    tags=['Товары'],
)
class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

@extend_schema(
    summary='Детальная информация о товаре',
    description='Возвращает полную информацию об одном товаре по id',
    tags=['Товары'],
)
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer