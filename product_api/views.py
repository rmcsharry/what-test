"""
This module defines the Product views.
"""
from rest_framework.permissions import AllowAny
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from django.db.models import Q

class ProductList(generics.ListAPIView):
    """
    API view to search products or return all products.
    """
    serializer_class = ProductSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned products to a given search term,
        by overriding the queryset.
        """
        search = self.request.query_params.get('search', None)
        if search is not None:
            queryset = Product.objects.filter(
                Q(name__icontains=search) |
                Q(description__icontains=search) |
                Q(price__icontains=search) |
                Q(stock__icontains=search)
            )
        else:
            queryset = Product.objects.all()
        return queryset

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update or delete a product.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
