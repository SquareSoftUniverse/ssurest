from rest_framework import viewsets

from chat_posts.models import ChatProfile, Handles, Posts, Rooms
from chat_posts.pagination import OrderedInReversePagination
from chat_posts.serializers import (
    ChatProfileSerializer,
    HandleSerializer,
    PostSerializer,
    RoomSerializer,
)


class ChatUserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ChatProfile.objects.all()
    serializer_class = ChatProfileSerializer


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
