from rest_framework import generics
from .models import Produto
from .serializers import ProdutoSerializer


class ProdutoListCreateView(generics.ListCreateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    def get_queryset(self):
        queryset = Produto.objects.all()
        categoria = self.request.query_params.get('categoria')

        if categoria:
            queryset = queryset.filter(categoria=categoria)

        return queryset
