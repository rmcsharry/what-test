"""
This module defines the ProductList view.
"""
from rest_framework.permissions import AllowAny
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

class ProductList(generics.ListCreateAPIView):
  """
  API view to retrieve list of products
  """
  permission_classes = (AllowAny, )
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
