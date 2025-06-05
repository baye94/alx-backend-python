# messaging_app/chats/permissions.py

from rest_framework import permissions
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Object-level permission for viewing/editing only own messages or conversations
        return obj.user == request.user

class IsParticipantOfConversation(BasePermission):
    """
    Allow only authenticated users who are participants of the conversation.
    """

    def has_permission(self, request, view):
        # Ensure the user is authenticated
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        """
        Object-level permission to only allow participants of the conversation
        to view, update, or delete messages.
        """
        conversation = getattr(obj, 'conversation', None)
        if conversation:
            return request.user in conversation.participants.all()
        return False