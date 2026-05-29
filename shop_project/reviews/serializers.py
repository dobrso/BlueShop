from rest_framework import serializers
from django.contrib.auth.models import User

from catalog.models import Product
from .models import Review


class UserShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class ProductShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title']

class ReviewSerializer(serializers.ModelSerializer):
    user = UserShortSerializer(read_only=True)
    product = ProductShortSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'text', 'rating', 'user', 'product']