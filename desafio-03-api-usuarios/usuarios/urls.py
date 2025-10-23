from django.urls import path
from .views import UsuarioCreateView, UsuarioListView


urlpatterns = [
    path('registrar/', UsuarioCreateView.as_view(), name='registrar'),
    path('usuarios/', UsuarioListView.as_view(), name='usuario-list'),
]
