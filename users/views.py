from rest_framework import generics
from users.serializers import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """
    API view for creating a new user.

    Allows the creation of a new user instance by sending a POST request with the required data.

    Parameters:
    - serializer_class: The serializer class for converting user data to and from JSON.

    Methods:
    Handles POST requests to create a new user instance.
    """
    serializer_class = UserSerializer
