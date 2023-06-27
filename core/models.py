from django.db import models
from django.contrib.auth import get_user_model
from room.models import Room

User = get_user_model()


# Create your models here.
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)
    text = models.TextField(null=True)

    def __str__(self) -> str:
        return str(self.id)


class FriendList(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="name")

    def __str__(self) -> str:
        return f"{self.user}"

class Friend(models.Model):
    friend = models.ForeignKey(User, on_delete=models.CASCADE)
    friendlist = models.ForeignKey(FriendList, on_delete=models.CASCADE)

class BanList(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username

class BanUser(models.Model):
    ban_friend = models.ForeignKey(User, on_delete=models.CASCADE)
    banlist = models.ForeignKey(BanList, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"banned user: {self.ban_friend} list of {self.banlist}"