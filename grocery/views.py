from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import GroceryItemSerializer
from .models import GroceryItem


class GroceryListAPIView(APIView):
    """List all grocery items or create new item"""

    def get(self, request):
        items = GroceryItem.objects.all()
        serializer = GroceryItemSerializer(items, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = GroceryItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Item added successfully!',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)