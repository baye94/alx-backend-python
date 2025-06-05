# chats/views.py

from rest_framework.viewsets import ModelViewSet
from .models import Message
from .serializers import MessageSerializer
from .permissions import IsParticipantOfConversation
from rest_framework.permissions import IsAuthenticated

class MessageViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated, IsParticipantOfConversation]

    def get_queryset(self):
        # Only return messages from conversations the user participates in
        return Message.objects.filter(conversation__participants=self.request.user)
