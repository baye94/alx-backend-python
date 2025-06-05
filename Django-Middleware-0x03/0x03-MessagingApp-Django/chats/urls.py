from django.urls import path, include
from rest_framework_nested import routers  # ✅ Nested router importé
from .views import UserViewSet, ConversationViewSet, MessageViewSet
from django.contrib import admin
from django.urls import path, include
from messaging_app.chats import auth

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
    path('admin/', admin.site.urls),
    path('api/token/', auth.token_obtain_pair, name='token_obtain_pair'),
    path('api/token/refresh/', auth.token_refresh, name='token_refresh'),
    path('api/', include('messaging_app.chats.urls')),
]
