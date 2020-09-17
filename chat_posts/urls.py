from django.urls import path, include
from rest_framework.routers import DefaultRouter
from chat_posts.views import ChatUserViewSet, HandleViewSet

router = DefaultRouter()
router.register(r'chat_users', ChatUserViewSet)
router.register(r'handles', HandleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]