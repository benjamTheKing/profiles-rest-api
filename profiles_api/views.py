from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test Api View"""
    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'uses HTTP methods as function (get, post, patch, put, delete)',
            'is similar to the traditional Django View',
            'give you control',
            'is mapped manually to Urls',
        ]
        return Response({'message':'hello', 'an_apiview': an_apiview})