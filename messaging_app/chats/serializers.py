from rest_framework import serializers
from .models import User, Conversation, Message


# 🔹 1. User Serializer
class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.CharField()
    phone_number = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = User
        fields = [
            'user_id', 'username', 'first_name', 'last_name', 'email',
            'phone_number', 'bio', 'profile_picture', 'is_online', 'last_seen'
        ]


# 🔹 2. Message Serializer
class MessageSerializer(serializers.ModelSerializer):
    sender_username = serializers.SerializerMethodField()
    message_body = serializers.CharField()
    sent_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Message
        fields = [
            'message_id', 'conversation', 'sender', 'sender_username',
            'message_body', 'sent_at', 'is_read', 'edited', 'attachment'
        ]

    def get_sender_username(self, obj):
        return obj.sender.username

    def validate_message_body(self, value):
        if not value.strip():
            raise serializers.ValidationError("Message body cannot be empty.")
        return value


# 🔹 3. Conversation Serializer
class ConversationSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=False)
    participants = UserSerializer(many=True, read_only=True)
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Conversation
        fields = [
            'conversation_id', 'title', 'is_group',
            'participants', 'messages', 'created_at', 'updated_at'
        ]
