from django.shortcuts import render
from rest_framework import viewsets, mixins
from .serializers import MessageSerializer, FriendListSerializer, FriendSerializer, BanListSerializer, BanUserSerializer 
from .models import Message, FriendList, Friend


# Create your views here.
class MessageViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = MessageSerializer
    lookup_field = "id"

    def get_queryset(self):
        room_id = self.request.query_params.get("room_id")
        queryset = Message.objects.filter(room__creator=self.request.user)

        if room_id:
            queryset = queryset.filter(room_id=room_id)

        return queryset

    # def delete(self, request, *args, **kwargs):
    # user = request.user
    # if user != Message.objects.get(user=request.user):
    # raise ValueError("error")
    # return super().delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        message_id = kwargs.get("pk")
        try:
            message = Message.objects.get(id=message_id, user=request.user)
        except Message.DoesNotExist:
            raise ValueError("Invalid message ID or user not authorized")

        return super().delete(request, *args, **kwargs)


class FriendListViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = FriendListSerializer
    lookup_field = "id"

    def get_queryset(self):
        return FriendList.objects.filter(user=self.request.user)


class FriendViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = FriendSerializer
    queryset = Friend.objects.all()
    lookup_field = "id"
