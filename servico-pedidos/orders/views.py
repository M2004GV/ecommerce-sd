import requests
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        # Validação via chamada HTTP síncrona aos outros microsserviços
        cliente_id = request.data.get('cliente_id', 1) 
        
        # Substitua a URL local pela URL pública do Render após o deploy dos novos serviços
        cliente_url = f"http://127.0.0.1:8001/clientes/{cliente_id}"
        
        try:
            # Tratamento básico de erro com timeout exigido pelo projeto
            resposta = requests.get(cliente_url, timeout=3)
            if resposta.status_code != 200:
                return Response({"erro": "Cliente inválido ou inexistente."}, status=status.HTTP_400_BAD_REQUEST)
        except requests.exceptions.RequestException:
            return Response(
                {"erro": "Serviço de clientes temporariamente indisponível. Tente novamente mais tarde."}, 
                status=status.HTTP_503_SERVICE_UNAVAILABLE
            )

        return super().create(request, *args, **kwargs)
