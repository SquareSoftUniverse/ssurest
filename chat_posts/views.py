from rest_framework import viewsets

from chat_posts.models import ChatUsers, Handles
from chat_posts.serializers import ChatUserSerializer, HandleSerializer


class ChatUserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ChatUsers.objects.all()
    serializer_class = ChatUserSerializer


class HandleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Handles.objects.all()
    serializer_class = HandleSerializer

