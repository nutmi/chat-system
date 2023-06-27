from django.shortcuts import render
from rest_framework import viewsets, mixins
from .serializers import RoomSerializer
from .models import Room


# Create your views here.
class RoomViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = RoomSerializer
    lookup_field = "id"

    def get_queryset(self):
        return Room.objects.filter(creator=self.request.user)

    # def perform_create(self, serializer):
    # creator = Room.objects.get(creator=self.request.user)
    # guest = self.request.data.get("guest")

    # if creator == guest:
    # raise ValueError("error")
    # serializer.save()

    def perform_create(self, serializer):
        creator = Room.objects.filter(creator=self.request.user).first()
        guest = self.request.data.get("guest")

        if creator is None:
            raise ValueError("Creator room not found")
        elif creator.id == guest:
            raise ValueError("Error: Creator and guest are the same")

        serializer.save()

    def delete(self, request, *args, **kwargs):
        user = request.user
        guest = request.data.get("guest")
        creator = request.data.get("creator")

        if user != creator or guest:
            raise ValueError("error")
        return super().delete(request, *args, **kwargs)
