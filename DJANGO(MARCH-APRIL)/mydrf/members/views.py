from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ExampleSerializer

class ExampleView(APIView):
    def post(self, request):
        serializer = ExampleSerializer(data=request.data)
        if serializer.is_valid():
            # Process valid data
            name = serializer.validated_data.get('name')
            age = serializer.validated_data.get('age')
            return Response({"name": name, "age": age}, status=200)
        else:
            # Handle invalid data
            return Response(serializer.errors, status=400)

