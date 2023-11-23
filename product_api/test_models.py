"""
This module contains test cases for the product api models in the application.

It uses Django's TestCase class.
"""
from django.test import TestCase
from .models import Product

class ProductModelTest(TestCase):
    """
    Test class for the Product model.
    """
    @classmethod
    def setUpTestData(cls):
        """
        Set up non-modified objects used by all test methods.
        """
        Product.objects.create(name='Test Product', description='Test Description', price=9.99, stock=100)

    def test_name_content(self):
        """
        Test the name field content.
        """
        product = Product.objects.get(id=1)
        expected_object_name = f'{product.name}'
        self.assertEqual(expected_object_name, 'Test Product')

    def test_description_content(self):
        """
        Test the description field content.
        """
        product = Product.objects.get(id=1)
        expected_object_description = f'{product.description}'
        self.assertEqual(expected_object_description, 'Test Description')

    def test_price_content(self):
        """
        Test the price field content.
        """
        product = Product.objects.get(id=1)
        expected_object_price = product.price
        self.assertEqual(float(expected_object_price), 9.99)

    def test_stock_content(self):
        """
        Test the stock field content.
        """
        product = Product.objects.get(id=1)
        expected_object_stock = product.stock
        self.assertEqual(expected_object_stock, 100)