from rest_framework import serializers
from chat_posts.models import Rooms, Posts, Handles, ChatProfile


class ChatProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatProfile
        exclude = ("password",)


class HandleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Handles
        fields = "__all__"


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    handle = HandleSerializer()
    room = RoomSerializer()

    class Meta:
        model = Posts
        fields = "__all__"
