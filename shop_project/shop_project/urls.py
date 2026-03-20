from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalog.urls'), name='catalog'),
    path('', include('orders.urls'), name='orders'),
    path('', include('reviews.urls'), name='reviews'),
    path('', include('users.urls'), name='users'),
]
