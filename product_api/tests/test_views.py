from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import Product
from user_api.models import AppUser

class ProductDetailTest(APITestCase):
    """
    Test class for the ProductDetail view.
    """
    @classmethod
    def setUpTestData(cls):
        """
        Set up non-modified objects used by all test methods.
        """
        Product.objects.create(name='Test Product', description='Test Description', price='9.99', stock=100)
        cls.user = AppUser.objects.create_user(email='testuser@test.com', password='testpass')

    def test_update_product(self):
        """
        Test updating a product via PATCH.
        """
        self.client.login(email='testuser@test.com', password='testpass')
        product = Product.objects.get(name='Test Product')
        url = reverse('product-detail', args=[product.id])
        data = {'selected': True}
        response = self.client.patch(url, data, format='json')
        product.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(product.selected, True)