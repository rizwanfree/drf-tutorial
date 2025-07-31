from django.shortcuts import get_object_or_404

from api.serializers import OrderSerializer, ProductSerializer
from api.models import Order, Product

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    serializer = ProductSerializer(product)
    return Response(data=serializer.data)



@api_view(['GET'])
def order_list(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(data=serializer.data)