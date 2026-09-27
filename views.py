"""
views.py — Contains all the view functions (Controller in MVC terms).

Each function:
  1. Receives an HTTP request
  2. Performs a database operation using Django ORM
  3. Returns an HTTP response (renders an HTML template)

CRUD operations:
  - room_list    → READ   (show all rooms)
  - room_create  → CREATE (add a new room)
  - room_update  → UPDATE (edit an existing room)
  - room_delete  → DELETE (remove a room)
"""

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Room
from .forms import RoomForm


# ──────────────────────────────────────────────
# READ — Show all rooms
# ──────────────────────────────────────────────
def room_list(request):
    """
    Fetch all Room records from the database and pass them to the template.
    Django ORM: Room.objects.all() → SELECT * FROM rooms_room;
    """
    rooms = Room.objects.all()
    return render(request, 'rooms/room_list.html', {'rooms': rooms})


# ──────────────────────────────────────────────
# CREATE — Add a new room
# ──────────────────────────────────────────────
def room_create(request):
    """
    GET  → Show an empty form.
    POST → Validate and save the new room to the database.
    """
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()                                        # INSERT INTO rooms_room ...
            messages.success(request, 'Room added successfully!')
            return redirect('room_list')
    else:
        form = RoomForm()                                      # Empty form for GET request

    return render(request, 'rooms/room_form.html', {'form': form, 'action': 'Add'})


# ──────────────────────────────────────────────
# UPDATE — Edit an existing room
# ──────────────────────────────────────────────
def room_update(request, pk):
    """
    pk  → Primary key (ID) of the room to edit.
    GET  → Show the form pre-filled with existing data.
    POST → Validate and update the database record.
    """
    room = get_object_or_404(Room, pk=pk)   # Fetch room or return 404 if not found

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)   # Bind form to existing instance
        if form.is_valid():
            form.save()                                # UPDATE rooms_room SET ... WHERE id=pk
            messages.success(request, 'Room updated successfully!')
            return redirect('room_list')
    else:
        form = RoomForm(instance=room)                 # Pre-fill form with existing data

    return render(request, 'rooms/room_form.html', {'form': form, 'action': 'Edit'})


# ──────────────────────────────────────────────
# DELETE — Remove a room
# ──────────────────────────────────────────────
def room_delete(request, pk):
    """
    GET  → Show a confirmation page ("Are you sure?").
    POST → Delete the room from the database.
    """
    room = get_object_or_404(Room, pk=pk)

    if request.method == 'POST':
        room.delete()                                  # DELETE FROM rooms_room WHERE id=pk
        messages.success(request, 'Room deleted successfully!')
        return redirect('room_list')

    return render(request, 'rooms/room_confirm_delete.html', {'room': room})
