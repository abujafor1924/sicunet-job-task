"""Views for Access Control System"""

from django.shortcuts import render
from access_control.models import AccessLog
from django_filters.rest_framework import DjangoFilterBackend
from access_control.serializers import AccessLogSerializer
from rest_framework import generics, status
from rest_framework.response import Response


class AccessLogListCreateView(generics.ListCreateAPIView):
    """View to list and create AccessLog entries."""
    queryset = AccessLog.objects.all()
    serializer_class = AccessLogSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['card_id', 'door_name', 'access_granted']

    def get_queryset(self):
        """Filter AccessLogs based on query parameters."""
        queryset = super().get_queryset()
        card_id = self.request.query_params.get('card_id')
        door_name = self.request.query_params.get('door_name')
        access_granted = self.request.query_params.get('access_granted')

        if card_id:
            queryset = queryset.filter(card_id=card_id)
        if door_name:
            queryset = queryset.filter(door_name=door_name)
        if access_granted is not None:
            if access_granted.lower() in ['true', '1', 'yes']:
                queryset = queryset.filter(access_granted=True)
            elif access_granted.lower() in ['false', '0', 'no']:
                queryset = queryset.filter(access_granted=False)

        return queryset

    def create(self, request, *args, **kwargs):
        """Create a new AccessLog entry."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(
            {"message": "AccessLog entry created successfully", "data": serializer.data},
            status=status.HTTP_201_CREATED
        )

    def list(self, request, *args, **kwargs):
        """List all AccessLog entries."""
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        return Response(
            {"data": serializer.data},
            status=status.HTTP_200_OK
        )


class AccessLogRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """View to retrieve, update, or delete an AccessLog entry."""
    queryset = AccessLog.objects.all()
    serializer_class = AccessLogSerializer

    def retrieve(self, request, *args, **kwargs):
        """Retrieve a specific AccessLog entry."""
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        return Response(
            {
                "message": "AccessLog entry retrieved successfully",
                "data": serializer.data},
            status=status.HTTP_200_OK
        )

    def update(self, request, *args, **kwargs):
        """Update a specific AccessLog entry."""
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(
            {
                "message": "AccessLog entry updated successfully",
                "data": serializer.data
            },
            status=status.HTTP_200_OK
        )

    def destroy(self, request, *args, **kwargs):
        """Delete a specific AccessLog entry."""
        instance = self.get_object()
        self.perform_destroy(instance)

        return Response(
            {"message": "AccessLog entry deleted successfully"},
            status=status.HTTP_200_OK
        )
