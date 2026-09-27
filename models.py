"""
models.py — Defines the Room database table using Django ORM.

When Django reads this file, it creates a table called 'rooms_room' in SQLite.
Each field maps to one column in that table.
"""

from django.db import models


class Room(models.Model):
    # Choices for room type (shown as a dropdown in forms)
    ROOM_TYPE_CHOICES = [
        ('Single', 'Single'),
        ('Double', 'Double'),
        ('Suite',  'Suite'),
        ('Deluxe', 'Deluxe'),
    ]

    room_number = models.CharField(max_length=10, unique=True)   # e.g. "101"
    room_type   = models.CharField(max_length=20, choices=ROOM_TYPE_CHOICES)
    price       = models.DecimalField(max_digits=8, decimal_places=2)  # e.g. 1500.00
    floor       = models.IntegerField()                                 # e.g. 1, 2, 3
    availability = models.BooleanField(default=True)                   # True = Available

    class Meta:
        ordering = ['floor', 'room_number']   # Default sort order

    def __str__(self):
        # This is shown in the Django admin list and shell repr
        return f"Room {self.room_number} ({self.room_type})"
