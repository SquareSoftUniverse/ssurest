from django.urls import path, include
from rest_framework.routers import DefaultRouter
from chat_posts.views import (
    ChatUserViewSet,
    HandleViewSet,
    PostViewSet,
    RoomViewSet,
    SSUPostViewSet,
)

router = DefaultRouter()
router.register(r"chat_users", ChatUserViewSet)
router.register(r"handles", HandleViewSet)
router.register(r"rooms", RoomViewSet)
router.register(r"posts", PostViewSet)
router.register(r"ssuposts", SSUPostViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
