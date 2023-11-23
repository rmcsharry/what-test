from django.test import TestCase
from user_api.serializers import UserRegisterSerializer, UserLoginSerializer, UserSerializer
from django.contrib.auth import get_user_model

class UserRegisterSerializerTest(TestCase):
  def setUp(self):
    self.data = {'email': 'testuser@test.com', 'username': 'test', 'password': 'testpassword123'}

  def test_create_user(self):
    serializer = UserRegisterSerializer(data=self.data)
    self.assertTrue(serializer.is_valid())
    user = serializer.save()
    self.assertEqual(user.email, self.data['email'])
    self.assertEqual(user.username, self.data['username'])

class UserLoginSerializerTest(TestCase):
  def setUp(self):
    self.user = get_user_model().objects.create_user(email='testuser@test.com', password='testpassword123')

  def test_check_user(self):
    data = {'email': 'testuser@test.com', 'password': 'testpassword123'}
    serializer = UserLoginSerializer(data=data)
    self.assertTrue(serializer.is_valid())
    user = serializer.check_user(serializer.validated_data)
    self.assertEqual(user, self.user)

class UserSerializerTest(TestCase):
  def setUp(self):
    self.user = get_user_model().objects.create_user(email='testuser@test.com', password='testpassword123')

  def test_user_serializer(self):
    serializer = UserSerializer(self.user)
    data = serializer.data
    self.assertEqual(data['email'], 'testuser@test.com')