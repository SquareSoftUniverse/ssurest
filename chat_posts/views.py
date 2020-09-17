from rest_framework import viewsets

from chat_posts.models import Handles
from chat_posts.serializers import HandleSerializer


class HandleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Handles.objects.all()
    serializer_class = HandleSerializer

