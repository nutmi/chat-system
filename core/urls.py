from django.contrib import admin
from django.urls import path
from rest_framework import routers
from .views import MessageViewSet, FriendListViewSet, FriendViewSet

router = routers.SimpleRouter()
router.register(r"message", MessageViewSet, basename="message")
router.register(r"friendlist", FriendListViewSet, basename="friendlist")
router.register(r"friend", FriendViewSet, basename="friend")
urlpatterns = router.urls
urlpatterns += []
