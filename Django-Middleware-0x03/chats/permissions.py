# chats/permissions.py

from rest_framework.permissions import BasePermission

class IsParticipantOfConversation(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        conversation = getattr(obj, 'conversation', None)
        if not conversation:
            return False

        # Explicitly handle methods: GET, PUT, PATCH, DELETE
        if request.method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
            return request.user in conversation.participants.all()

        return False
