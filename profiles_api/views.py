from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloApiView(APIView):
    """Test API View."""

    def get(self, request, format=None):
        """Returns a list of APIView features."""
        serializer_class = serializers.HelloSerializer

        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        # Response must be a dictionary or a list
        return Response({'message': 'Hello!', 'an_apiview': an_apiview}) # Response is required for APIView
    
    def post(self, request):
        """Create a hello message with our name."""
        serializer = serializers.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!' # f is required for string interpolation
            return Response({'message': message})