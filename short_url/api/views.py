from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView

from .serializers import ShortURLCreateSerializer


class ShortURLCreateAPIView(CreateAPIView):
    serializer_class = ShortURLCreateSerializer
    permission_classes = (IsAuthenticated,)
