"""
This module defines API views for user registration, login, logout, and retrieval.

The UserRegister view handles user registration.
The UserLogin view handles user login.
The UserLogout view handles user logout.
The UserView retrieves the authenticated user's data.
"""

from django.contrib.auth import login, logout
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from .serializers import UserRegisterSerializer, UserLoginSerializer, UserSerializer

class UserRegister(APIView):
    """
    API view for user registration.
    """
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication,)

    def post(self, request):
        """
        Register a new user.
        """
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.create(request.data)
            if user:
                login(request, user) # Manually log the user in after registration
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):
    """
    API view for user login.
    """
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication,)

    def post(self, request):
        """
        Log in a user.
        """
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.check_user(request.data)
            login(request, user)
            return Response(serializer.data, status=status.HTTP_200_OK)


class UserLogout(APIView):
    """
    API view for user logout.
    """
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request):
        """
        Log out a user.
        """
        logout(request)
        response = Response(status=status.HTTP_200_OK)
        response.delete_cookie('csrftoken')
        return response


class UserView(APIView):
    """
    API view for retrieving the authenticated user's data.
    """
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)

    def get(self, request):
        """
        Retrieve the authenticated user's data.
        """
        serializer = UserSerializer(request.user)
        return Response({'user': serializer.data}, status=status.HTTP_200_OK)
