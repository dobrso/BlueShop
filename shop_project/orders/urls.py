from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views, api_views

app_name = 'orders'

router = DefaultRouter()
router.register(r'orders', api_views.OrderViewSet, basename='order')

urlpatterns = [
    path('list/', views.order_list, name='order_list'),
    path('api/orders/', api_views.OrderListAPIView.as_view(), name='api_orders'),
    path('api/orders/<int:pk>/', api_views.OrderDetailAPIView.as_view(), name='api_order_detail'),
    path('api/', include(router.urls)),
]