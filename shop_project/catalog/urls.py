from django.urls import path

from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.home_page, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
]