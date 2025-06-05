# messaging_app/chats/permissions.py

from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Object-level permission for viewing/editing only own messages or conversations
        return obj.user == request.user
