"""
This module contains test cases for the serializers in the application.

It uses Django's TestCase class.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from user_api.serializers import UserRegisterSerializer, UserLoginSerializer, UserSerializer

class UserRegisterSerializerTest(TestCase):
    """
    Test case for the UserRegisterSerializer.
    """

    def setUp(self):
        """
        Set up the test case with test data.
        """
        self.data = {'email': 'testuser@test.com',
                     'username': 'test', 'password': 'testpassword123'}

    def test_create_user(self):
        """
        Test the creation of a user using the UserRegisterSerializer.
        """
        serializer = UserRegisterSerializer(data=self.data)
        self.assertTrue(serializer.is_valid())
        user = serializer.save()
        self.assertEqual(user.email, self.data['email'])
        self.assertEqual(user.username, self.data['username'])


class UserLoginSerializerTest(TestCase):
    """
    Test case for the UserLoginSerializer.
    """

    def setUp(self):
        """
        Set up the test case with a test user.
        """
        self.user = get_user_model().objects.create_user(
            email='testuser@test.com', password='testpassword123')

    def test_check_user(self):
        """
        Test the checking of a user using the UserLoginSerializer.
        """
        data = {'email': 'testuser@test.com', 'password': 'testpassword123'}
        serializer = UserLoginSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        user = serializer.check_user(serializer.validated_data)
        self.assertEqual(user, self.user)


class UserSerializerTest(TestCase):
    """
    Test case for the UserSerializer.
    """

    def setUp(self):
        """
        Set up the test case with a test user.
        """
        self.user = get_user_model().objects.create_user(
            email='testuser@test.com', password='testpassword123')

    def test_user_serializer(self):
        """
        Test the serialization of a user using the UserSerializer.
        """
        serializer = UserSerializer(self.user)
        data = serializer.data
        self.assertEqual(data['email'], 'testuser@test.com')
