from django.test import TestCase
from ..models import Product
from ..serializers import ProductSerializer

class ProductSerializerTest(TestCase):
    """
    Test class for the ProductSerializer.
    """
    @classmethod
    def setUpTestData(cls):
        """
        Set up non-modified objects used by all test methods.
        """
        cls.product = Product.objects.create(name='Test Product', description='Test Description', price='9.99', stock=100, selected=False)

    def test_product_serializer(self):
        """
        Test serializing a product.
        """
        serializer = ProductSerializer(self.product)
        expected_data = {
            'id': self.product.id,
            'name': 'Test Product',
            'description': 'Test Description',
            'price': '9.99',
            'stock': 100,
            'selected': False
        }
        self.assertEqual(serializer.data, expected_data)