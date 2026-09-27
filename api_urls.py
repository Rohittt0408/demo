"""
api_urls.py — URL patterns for the REST API endpoints.
"""

from django.urls import path
from .api_views import RoomListCreateAPIView, RoomDetailAPIView

urlpatterns = [
    # GET all rooms / POST create a room
    path('rooms/', RoomListCreateAPIView.as_view(), name='api_room_list'),

    # GET / PUT / DELETE a single room by ID
    path('rooms/<int:pk>/', RoomDetailAPIView.as_view(), name='api_room_detail'),
]
