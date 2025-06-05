import django_filters
from .models import Message
from django.contrib.auth.models import User

class MessageFilter(django_filters.FilterSet):
    sender = django_filters.ModelChoiceFilter(queryset=User.objects.all())
    conversation = django_filters.NumberFilter(field_name='conversation__id')
    date_min = django_filters.DateTimeFilter(field_name='timestamp', lookup_expr='gte')
    date_max = django_filters.DateTimeFilter(field_name='timestamp', lookup_expr='lte')

    class Meta:
        model = Message
        fields = ['sender', 'conversation', 'date_min', 'date_max']
