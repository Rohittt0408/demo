"""
serializers.py — Converts Room model instances to/from JSON for the REST API.

A Serializer is like a translator:
  Python object  →  JSON  (for API responses)
  JSON           →  Python object  (for API input)
"""

from rest_framework import serializers
from .models import Room


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Room
        fields = '__all__'   # Include all fields: id, room_number, room_type, price, floor, availability
