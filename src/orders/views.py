from rest_framework.views import Response, APIView
from .models import Order
from .serializers import OrderSerializer,OrderItemSerializer


class OrderItemCartView(APIView):
    pass



class ShoppingCartView(APIView):
    def get(self,request):
        pass

    def post(self, request):
        serializer_order=OrderSerializer(data=request.data)
        serializer_order.is_valid(raise_exception=True)
        print(serializer_order.data)
