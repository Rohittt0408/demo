"""
api_views.py — REST API views using Django REST Framework.

We use APIView (class-based) to handle JSON requests.

Endpoints:
  GET  /api/rooms/      → List all rooms as JSON
  POST /api/rooms/      → Create a new room via JSON

  GET    /api/rooms/<id>/  → Get one room
  PUT    /api/rooms/<id>/  → Update a room
  DELETE /api/rooms/<id>/  → Delete a room
"""

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Room
from .serializers import RoomSerializer


# ──────────────────────────────────────────────
# /api/rooms/ — List all & Create
# ──────────────────────────────────────────────
class RoomListCreateAPIView(APIView):

    def get(self, request):
        """Return all rooms as a JSON array."""
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)   # many=True → list of objects
        return Response(serializer.data)

    def post(self, request):
        """Create a new room from JSON body."""
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ──────────────────────────────────────────────
# /api/rooms/<id>/ — Retrieve, Update, Delete
# ──────────────────────────────────────────────
class RoomDetailAPIView(APIView):

    def get(self, request, pk):
        """Return a single room as JSON."""
        room = get_object_or_404(Room, pk=pk)
        serializer = RoomSerializer(room)
        return Response(serializer.data)

    def put(self, request, pk):
        """Update an existing room from JSON body."""
        room = get_object_or_404(Room, pk=pk)
        serializer = RoomSerializer(room, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Delete a room."""
        room = get_object_or_404(Room, pk=pk)
        room.delete()
        return Response({'message': 'Room deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
