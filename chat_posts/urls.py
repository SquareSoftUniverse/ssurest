from django.urls import path, include
from rest_framework.routers import DefaultRouter
from chat_posts.views import HandleViewSet

router = DefaultRouter()
router.register(r'handles', HandleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]