from random import choice, randint

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from users.models import Profile
from catalog.models import Category, Product
from orders.models import Order, OrderItem
from reviews.models import Review


class Command(BaseCommand):
    def handle(self, *args, **options):
        users = self._create_users()
        categories = self._create_categories()
        products = self._create_products(categories)
        self._create_orders(users, products)
        self._create_reviews(users, products)

        self.stdout.write(self.style.SUCCESS('БД заполнена'))

    def _create_users(self):
        User = get_user_model()
        users = []

        if not User.objects.filter(username='admin').exists():
            admin = User.objects.create_superuser(username='admin', email='admin@example.com', password='admin123')
            Profile.objects.get_or_create(user=admin)
            self.stdout.write('Создан суперюзер')

        for i in range(1, 4):
            user, created = User.objects.get_or_create(username = f'user{i}', defaults={'email': f'user{i}@example.com'})

            if created:
                user.set_password('qwerty123')
                user.save()
                Profile.objects.get_or_create(user=user)
                self.stdout.write(f'Создан юзер {user.username}')
            users.append(user)
        return users

    def _create_categories(self):
        names = ['Сумки', 'Одежда', 'Обувь']
        categories = []

        for name in names:
            cat, _ = Category.objects.get_or_create(name=name, defaults={'slug': name.lower()})
            categories.append(cat)
        self.stdout.write('Созданы категории')
        return categories

    def _create_products(self, categories):
        titles = ['Синий товар 1', 'Синий товар 2', 'Синий товар 3']
        products = []

        for i in range(10):
            cat = choice(categories)
            prod, _ = Product.objects.get_or_create(
                title=choice(titles),
                defaults={
                    'category': cat,
                    'description': 'Супер классный товар!',
                    'price': randint(1000, 5000),
                    'stock': randint(5, 20),
                }
            )
            products.append(prod)
        self.stdout.write('Созданы товары')
        return products

    def _create_orders(self, users, products):
        for i in range(3):
            user = choice(users)
            order = Order.objects.create(user=user)
            OrderItem.objects.create(
                order=order,
                product=choice(products),
                price = 1000,
                quantity = 1
            )
        self.stdout.write('Созданы заказы')

    def _create_reviews(self, users, products):
        for i in range(5):
            Review.objects.get_or_create(
                user=choice(users),
                product=choice(products),
                defaults={'text': 'Все супер!', 'rating': 5}
            )
        self.stdout.write('Созданы отзывы')

