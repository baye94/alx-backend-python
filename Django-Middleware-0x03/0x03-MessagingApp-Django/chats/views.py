# chats/views.py

from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import Message, Conversation
from .serializers import MessageSerializer
from .permissions import IsParticipantOfConversation
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import Message
from .serializers import MessageSerializer
from .permissions import IsParticipantOfConversation
from rest_framework.permissions import IsAuthenticated
from .filters import MessageFilter
from django_filters.rest_framework import DjangoFilterBackend
from .pagination import StandardResultsSetPagination

class MessageViewSet(ModelViewSet):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated, IsParticipantOfConversation]
    permission_classes = [IsAuthenticated, IsParticipantOfConversation]
    filter_backends = [DjangoFilterBackend]
    filterset_class = MessageFilter
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return Message.objects.filter(conversation__participants=self.request.user)

    def perform_create(self, serializer):
        conversation_id = self.request.data.get('conversation')

        if not conversation_id:
            return Response({'error': 'conversation_id is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            conversation = Conversation.objects.get(id=conversation_id)
        except Conversation.DoesNotExist:
            return Response({'error': 'Conversation not found'}, status=status.HTTP_404_NOT_FOUND)

        if self.request.user not in conversation.participants.all():
            return Response({'error': 'You are not a participant in this conversation'},
                            status=status.HTTP_403_FORBIDDEN)

        serializer.save(sender=self.request.user, conversation=conversation)


    def get_queryset(self):
        return Message.objects.filter(conversation__participants=self.request.user)
