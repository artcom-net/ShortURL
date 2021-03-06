from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from .serializers import UserCreateSerializer


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    permission_classes = (AllowAny,)
