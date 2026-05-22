from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views, api_views

router = DefaultRouter()
router.register(r'reviews', api_views.ReviewViewSet, basename='review')

app_name = 'reviews'

urlpatterns = [
    path('all/', views.review_list, name='review_list'),
    path('product/<int:product_id>/add/', views.add_review, name='add_review'),
    path('<int:review_id>/edit/', views.edit_review, name='edit_review'),
    path('<int:review_id>/delete/', views.delete_review, name='delete_review'),
    path('api/reviews/', api_views.ReviewListAPIView.as_view(), name='api_reviews'),
    path('api/reviews/<int:pk>/', api_views.ReviewDetailAPIView.as_view(), name='api_review_detail'),
    path('api/', include(router.urls)),
]
