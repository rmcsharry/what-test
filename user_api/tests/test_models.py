from django.test import TestCase
from user_api.models import AppUser

class AppUserModelTest(TestCase):
    def setUp(self):
        self.user = AppUser.objects.create(
            email='testuser@test.com',
            username='testuser',
            password='testpassword123'
        )

    def test_create_user(self):
        self.assertEqual(AppUser.objects.count(), 1)
        self.assertEqual(self.user.email, 'testuser@test.com')
        self.assertEqual(self.user.username, 'testuser')

    def test_user_str(self):
        self.assertEqual(str(self.user), 'testuser')

    def test_required_fields(self):
        self.assertEqual(AppUser.REQUIRED_FIELDS, ['username'])

    def test_username_field(self):
        self.assertEqual(AppUser.USERNAME_FIELD, 'email')

    def test_default_is_staff(self):
        self.assertFalse(self.user.is_staff)