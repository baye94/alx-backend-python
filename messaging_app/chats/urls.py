from django.urls import path, include
from rest_framework import routers  # ✅ Import correct
from .views import UserViewSet, ConversationViewSet, MessageViewSet

# ✅ Déclaration explicite du routeur
router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'conversations', ConversationViewSet, basename='conversation')
router.register(r'messages', MessageViewSet, basename='message')

urlpatterns = [
    path('', include(router.urls)),  # ✅ Inclusion du router
]
