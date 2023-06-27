from django.contrib import admin
from .models import Message, FriendList, Friend, BanList, BanUser

# Register your models here.
admin.site.register(Message)
admin.site.register(FriendList)
admin.site.register(Friend)
admin.site.register(BanList)
admin.site.register(BanUser)
