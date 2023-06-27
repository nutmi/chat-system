from rest_framework import serializers
from .models import Message, FriendList, Friend, BanList, BanUser

class BanListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BanList
        fields = "__all__"
class BanUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BanUser
        fields = "__all__"

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ["text", "user", "room"]


class FriendListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendList
        fields = ["user", "friend"]


class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = ["friend", "friendlist"]
