from decimal import Decimal

import pytest
from django.contrib.auth import get_user_model

from catalog.models import Category, Product
from orders.models import Order, OrderItem
from reviews.models import Review
from users.models import Profile

User = get_user_model()

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
    )

@pytest.fixture
def user(db):
    return User.objects.create_user(username='alice', password='pass123')

@pytest.fixture
def order(db, user):
    return Order.objects.create(user=user)

@pytest.mark.django_db
class TestCategory:
    def test_str(self, category):
        assert str(category) == 'Смартфоны'

@pytest.mark.django_db
class TestOrderItem:
    def test_price_snapshot(self, order, product):
        item = OrderItem.objects.create(
            order=order,
            product=product,
            price=Decimal('12345.00'),
            quantity=1,
        )

        product.price = Decimal('1.00')
        product.save()
        item.refresh_from_db()
        assert item.price == Decimal('12345.00')

@pytest.mark.django_db
class TestProfileSignals:
    def test_auto_created_on_user_create(self):
        new_user = User.objects.create_user(username='bob', password='pass')
        assert Profile.objects.filter(user=new_user).exists()

@pytest.mark.django_db
class TestReview:
    def test_one_review_per_user(self, user, product):
        review = Review.objects.create(
            product=product,
            user=user,
            text='WW Product',
            rating=Decimal('5.00'),
        )
        assert Review.objects.filter(user=user, product=product).count() == 1