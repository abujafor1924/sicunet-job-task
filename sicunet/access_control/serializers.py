"""Serializers for Access Control System"""

from rest_framework import serializers
from access_control.models import AccessLog


class AccessLogSerializer(serializers.ModelSerializer):
    """Serializer for AccessLog model."""
    class Meta:
        """Meta class for AccessLogSerializer."""
        model = AccessLog
        fields = [
            'id','card_id', 'door_name', 'access_granted', 'timestamp'
        ]
        read_only_fields = ['id', 'timestamp']
        
            