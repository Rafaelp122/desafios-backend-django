from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import UserSerializer


class UsuarioCreateView(generics.CreateAPIView):
    """
    View para criar (registrar) um novo usuário.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = [AllowAny]


class UsuarioListView(generics.ListAPIView):
    """
    View para listar todos os usuários.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = [IsAuthenticated]
