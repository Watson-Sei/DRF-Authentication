from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Message
from .serializers import MessageSerializer
from rest_framework.permissions import IsAuthenticated


class MessageViewSet(viewsets.ModelViewSet):
    permission_classes = [
        IsAuthenticated
    ]

    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class HelloView(APIView):
    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)
