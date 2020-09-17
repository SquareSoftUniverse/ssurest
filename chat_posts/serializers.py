from rest_framework import serializers
from chat_posts.models import Rooms, Posts, Handles, ChatUsers


class HandleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Handles
        fields = '__all__'