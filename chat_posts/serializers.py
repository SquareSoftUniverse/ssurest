from rest_framework import serializers
from chat_posts.models import Rooms, Posts, Handles, ChatUsers


class ChatUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatUsers
        exclude = ("password",)


class HandleSerializer(serializers.ModelSerializer):
    chat_user = ChatUserSerializer()

    class Meta:
        model = Handles
        fields = "__all__"
