"""
This module contains test cases for the views in the application.

It uses Django's TestCase class and the DRF APIClient for simulating HTTP requests.
"""
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status


class UserRegisterViewTest(TestCase):
    """
    Test case for the UserRegisterView.
    """

    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse('register')
        self.data = {'email': 'testuser@test.com',
                     'username': 'test', 'password': 'testpassword123'}

    def test_register_user(self):
        """
        Test the user register process.

        This test creates a test user, sends a POST request to the register endpoint with the test user's
        credentials, and then verifies the response. The test passes if the response status code is 201, 
        indicating that the registration was successful.
        """
        response = self.client.post(self.register_url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(get_user_model().objects.count(), 1)
        self.assertEqual(get_user_model().objects.get().email,
                         'testuser@test.com')


class UserLoginViewTest(TestCase):
    """
    Test case for the UserLoginView.
    """

    def setUp(self):
        self.client = APIClient()
        self.login_url = reverse('login')
        self.user = get_user_model().objects.create_user(
            email='testuser@test.com', password='testpassword123')
        self.data = {'email': 'testuser@test.com',
                     'password': 'testpassword123'}

    def test_login_user(self):
        """
        Test the user login process.

        This test creates a test user, sends a POST request to the login endpoint with the test user's 
        credentials, and then verifies the response. The test passes if the response status code is 200, 
        indicating that the login was successful.
        """
        response = self.client.post(self.login_url, self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UserLogoutViewTest(TestCase):
    """
    Test case for the UserLogoutView.
    """

    def setUp(self):
        self.client = APIClient()
        self.logout_url = reverse('logout')
        self.user = get_user_model().objects.create_user(
            email='testuser@test.com', password='testpassword123')
        self.client.force_authenticate(user=self.user)

    def test_logout_user(self):
        """
        Test the user lgout process.

        This test creates a test user, sends a POST request to the login endpoint with the test user's 
        credentials, and then verifies the response. The test passes if the response status code is 200, 
        indicating that the login was successful.
        """
        response = self.client.post(self.logout_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UserViewTest(TestCase):
    """
    Test case for the UserView.
    """

    def setUp(self):
        self.client = APIClient()
        self.user_url = reverse('user')
        self.user = get_user_model().objects.create_user(
            email='testuser@test.com', password='testpassword123')
        self.client.force_authenticate(user=self.user)

    def test_get_user(self):
        """
        Test the user retrieval process.

        This test sends a GET request to the user endpoint and verifies the response.
        The test passes if the response status code is 200, indicating that the user data was 
        successfully retrieved.
        """
        response = self.client.get(self.user_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
