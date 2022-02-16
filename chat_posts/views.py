from rest_framework import viewsets

from chat_posts.models import ChatUsers, Handles, Posts, Rooms
from chat_posts.pagination import OrderedInReversePagination
from chat_posts.serializers import (
    ChatUserSerializer,
    HandleSerializer,
    PostSerializer,
    RoomSerializer,
)


class ChatUserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ChatUsers.objects.all()
    serializer_class = ChatUserSerializer


class HandleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Handles.objects.all()
    serializer_class = HandleSerializer


class RoomViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Rooms.objects.all()
    serializer_class = RoomSerializer


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Posts.objects.filter(room__id=2)
    serializer_class = PostSerializer
    pagination_class = OrderedInReversePagination
