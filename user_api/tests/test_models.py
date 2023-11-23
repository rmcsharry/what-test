"""
This module contains test cases for the user api models in the application.

It uses Django's TestCase class.
"""
from django.test import TestCase
from user_api.models import AppUser

class AppUserModelTest(TestCase):
    """
    Test case for the AppUser model.
    """
    def setUp(self):
        """
        Set up the test case with a test user.
        """
        self.user = AppUser.objects.create(
            email='testuser@test.com',
            username='testuser',
            password='testpassword123'
        )

    def test_create_user(self):
        """
        Test the creation of a user.
        """
        self.assertEqual(AppUser.objects.count(), 1)
        self.assertEqual(self.user.email, 'testuser@test.com')
        self.assertEqual(self.user.username, 'testuser')

    def test_user_str(self):
        """
        Test the string representation of a user.
        """
        self.assertEqual(str(self.user), 'testuser')

    def test_required_fields(self):
        """
        Test the required fields of a user.
        """
        self.assertEqual(AppUser.REQUIRED_FIELDS, ['username'])

    def test_username_field(self):
        """
        Test the username field of a user.
        """
        self.assertEqual(AppUser.USERNAME_FIELD, 'email')

    def test_default_is_staff(self):
        """
        Test the default is_staff value of a user.
        """
        self.assertFalse(self.user.is_staff)
