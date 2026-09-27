"""
admin.py — Registers the Room model with Django's built-in admin panel.

After registering, you can go to http://127.0.0.1:8000/admin/
and manage rooms through a ready-made UI without writing any extra code.
"""

from django.contrib import admin
from .models import Room


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    # Columns to show in the admin list view
    list_display  = ('room_number', 'room_type', 'price', 'floor', 'availability')

    # Add filter panel on the right side
    list_filter   = ('room_type', 'availability', 'floor')

    # Enable search by room number and type
    search_fields = ('room_number', 'room_type')

    # Allow toggling availability directly from the list
    list_editable = ('availability',)
