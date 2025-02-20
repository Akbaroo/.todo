from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .serializers import TodoSerializer
from .models import Todo

class TodoView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        data = Todo.objects.filter(user=user)
        ser = TodoSerializer(data, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        user = request.user
        title = request.data.get('title', {'title': ['This field is required.']})
        description = request.data.get('description', {'description': ['This field is required.']})
        
        if type(description) == dict:
            return Response(description, status=status.HTTP_400_BAD_REQUEST)

        if type(title) == dict:
            return Response(title, status=status.HTTP_400_BAD_REQUEST)
        if len(title) > 100:
            return Response({'detail':'max lengt is 100'}, status=status.HTTP_400_BAD_REQUEST)

        todo = Todo.objects.create(
            user=user,
            title=title,
            description=description,
)
        todo.save()
        return Response(status=status.HTTP_201_CREATED)

