from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import filters
from rest_framework import status


from .models import Product
from .serializers import ProductListSerializer, SearchProductSerializer


class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        if products:
            serializer = ProductListSerializer(products, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

class SearchProductView(APIView):
    def post(self, request):
        serializer=SearchProductSerializer(data=request.data)
        if serializer.is_valid():
            products=Product.objects.filter(name__contains= serializer.data.get('name'))
            if products:
                serializer = ProductListSerializer(products, many=True)
                return Response(serializer.data)
            return Response (status=status.HTTP_404_NOT_FOUND)


