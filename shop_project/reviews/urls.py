from django.urls import path

from . import views

app_name = 'reviews'

urlpatterns = [
    path('all/', views.review_list, name='review_list'),
]
