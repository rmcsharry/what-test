"""
This module defines serializers for user registration, login, and representation.

The UserRegisterSerializer is a ModelSerializer that creates a new user with the provided data.
The UserLoginSerializer is a Serializer that checks a user's credentials and raises a 
ValidationError if the user is not found.
The UserSerializer is a ModelSerializer that represents a user's email and username.
"""

from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth import get_user_model, authenticate

UserModel = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration.
    """
    class Meta:
        model = UserModel
        fields = '__all__'

    def create(self, clean_data):
        """
        Create a new user with the provided data.
        """
        user_obj = UserModel.objects.create_user(
            email=clean_data['email'], password=clean_data['password'])
        user_obj.username = clean_data['username']
        user_obj.save()
        return user_obj


class UserLoginSerializer(serializers.Serializer):
    """
    Serializer for user login.
    """
    email = serializers.EmailField()
    password = serializers.CharField()

    def check_user(self, clean_data):
        """
        Check a user's credentials and raise a ValidationError if the user is not found.
        """
        user = authenticate(
            username=clean_data['email'], password=clean_data['password'])
        if not user:
            raise ValidationError('user not found')
        return user


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for representing a user's email and username.
    """
    class Meta:
        model = UserModel
        fields = ('email', 'username')