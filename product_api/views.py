"""
This module defines the Product views.
"""
from rest_framework.permissions import AllowAny
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer


class ProductList(generics.ListCreateAPIView):
    """
    API view to retrieve list of products
    """
    # permission_classes = (AllowAny, )
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update or delete a product.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
