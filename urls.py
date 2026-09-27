"""
urls.py — URL patterns for the rooms app HTML views.

Each path() maps a URL to a view function.
"""

from django.urls import path
from . import views

urlpatterns = [
    # Home page — shows all rooms
    path('', views.room_list, name='room_list'),

    # Add a new room
    path('rooms/add/', views.room_create, name='room_create'),

    # Edit an existing room (pk = room's primary key / ID)
    path('rooms/edit/<int:pk>/', views.room_update, name='room_update'),

    # Delete a room
    path('rooms/delete/<int:pk>/', views.room_delete, name='room_delete'),
]
