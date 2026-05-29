from decimal import Decimal

import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

from catalog.models import Category, Product
from orders.models import Order
from reviews.models import Review

User = get_user_model()

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def category(db):
    return Category.objects.create(name='Смартфоны', slug='smartphones')

@pytest.fixture
def product(db, category):
    return Product.objects.create(
        category=category,
        title='IPhone 15',
        description='Крутой телефон',
        price=Decimal('99999.99'),
        stock=10,
        is_available=True,
    )

@pytest.fixture
def user(db):
    return User.objects.create_user(
        username='alice',
        password='pass123',
        email='alice@example.com',
    )

@pytest.fixture
def order(db, user):
    return Order.objects.create(user=user)

@pytest.fixture
def review(db, user, product):
    return Review.objects.create(
        user=user,
        product=product,
        text='ЗАВОЗИК WW',
        rating=5,
    )

@pytest.mark.django_db
def test_products_api_returns_list(api_client, product):
    url = reverse('catalog:api_products')
    response = api_client.get(url)
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]['title'] == 'IPhone 15'
    assert data[0]['price'] == '99999.99'

@pytest.mark.django_db
def test_api_me_returns_profile_for_authenticated_user(api_client, user):
    api_client.force_authenticate(user=user)
    url = reverse('users:api_my_profile')
    response = api_client.get(url)
    assert response.status_code == 200
    data = response.json()
    assert data['user']['username'] == user.username
    assert 'phone' in data
    assert 'address' in data

@pytest.mark.django_db
def test_category_api_returns_list(api_client, category):
    url = reverse('catalog:api_categories')
    response = api_client.get(url)
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]['slug'] == 'smartphones'

@pytest.mark.django_db
def test_orders_api_returns_list(api_client, user, order):
    url = reverse('orders:api_orders')
    response = api_client.get(url)
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]['user']['username'] == user.username

@pytest.mark.django_db
def test_review_api_returns_list(api_client, user, product, review):
    url = reverse('reviews:api_reviews')
    response = api_client.get(url)
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert 'product' in data[0]
    assert data[0]['product']['title'] == product.title
    assert data[0]['rating'] == 5