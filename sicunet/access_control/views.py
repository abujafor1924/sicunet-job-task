"""Views for Access Control System"""

from django.shortcuts import render
from access_control.models import AccessLog
from access_control.serializers import AccessLogSerializer
from rest_framework import generics, status
from rest_framework.response import Response


class AccessLogListCreateView(generics.ListCreateAPIView):
    """View to list and create AccessLog entries."""
    queryset = AccessLog.objects.all()
    serializer_class = AccessLogSerializer

    def create(self, request, *args, **kwargs):
        """Create a new AccessLog entry."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(
            {
                "message": "Access log created successfully",
                "data": serializer.data
            },
            status=status.HTTP_201_CREATED
        )

    def list(self, request, *args, **kwargs):
        """List all AccessLog entries."""
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        return Response(
            {
                "message": "Access logs fetched successfully",
                "data": serializer.data
            },
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
                "message": "Access log fetched successfully",
                "data": serializer.data
            },
            status=status.HTTP_200_OK
        )

    def update(self, request, *args, **kwargs):
        """Update a specific AccessLog entry."""
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance,
            data=request.data,
            partial=partial
        )
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(
            {
                "message": "Access log updated successfully",
                "data": serializer.data
            },
            status=status.HTTP_200_OK
        )

    def destroy(self, request, *args, **kwargs):
        """Delete a specific AccessLog entry."""
        instance = self.get_object()
        self.perform_destroy(instance)

        return Response(
            {
                "message": "Access log deleted successfully"
            },
            status=status.HTTP_204_NO_CONTENT
        )
