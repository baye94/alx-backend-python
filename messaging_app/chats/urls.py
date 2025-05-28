from django.urls import path, include
from rest_framework_nested import routers  # ✅ Nested router importé
from .views import UserViewSet, ConversationViewSet, MessageViewSet

# ✅ Routeur principal
router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'conversations', ConversationViewSet, basename='conversation')

# ✅ Routeur imbriqué : messages dans une conversation
conversation_router = routers.NestedDefaultRouter(router, r'conversations', lookup='conversation')
conversation_router.register(r'messages', MessageViewSet, basename='conversation-messages')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(conversation_router.urls)),
]
