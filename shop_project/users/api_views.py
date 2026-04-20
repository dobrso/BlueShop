from rest_framework import generics, permissions
from drf_spectacular.utils import extend_schema

from .models import Profile
from .serializers import ProfileSerializer

@extend_schema(
    summary='Профиль текущего пользователя',
    description=(
        'Возвращает профиль авторизованного пользователя: '
        'логин, email, телефон и адрес доставки. Требует аутентификацию'
    ),
    tags=['Пользователи'],
)
class MyProfileAPIView(generics.RetrieveAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return Profile.objects.get(user=self.request.user)