from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Room(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="creator")
    guest = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, related_name="guest"
    )
    title = models.CharField(max_length=100, null=True)

    def __str__(self) -> str:
        return str(self.id)
