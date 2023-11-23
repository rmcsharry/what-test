"""
This module defines the AppUser model and its manager, AppUserManager.

The AppUser model extends Django's AbstractBaseUser and PermissionsMixin to include 
additional fields. The AppUserManager provides methods for creating users and superusers.
"""

from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class AppUserManager(BaseUserManager):
    """
    Custom manager for AppUser model with email as the unique identifier.
    """
    def create_user(self, email, password=None):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError('An email is required.')
        if not password:
            raise ValueError('A password is required.')
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.is_staff = False
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None):
        """
        Create and save a SuperUser with the given email and password.
        """
        if not email:
            raise ValueError('An email is required.')
        if not password:
            raise ValueError('A password is required.')
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class AppUser(AbstractBaseUser, PermissionsMixin):
    """
    Custom User model where email is the unique identifier.
    """
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=50, unique=True)
    username = models.CharField(max_length=50)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = AppUserManager()

    def __str__(self):
        """
        String representation of the user model.
        """
        return self.username
