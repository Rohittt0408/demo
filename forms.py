"""
forms.py — A ModelForm that auto-generates an HTML form from the Room model.

Django ModelForm automatically creates input fields matching the model fields.
We don't have to write HTML <input> tags manually.
"""

from django import forms
from .models import Room


class RoomForm(forms.ModelForm):
    class Meta:
        model  = Room
        fields = ['room_number', 'room_type', 'price', 'floor', 'availability']

        # Add CSS classes and placeholders to each input for nicer styling
        widgets = {
            'room_number': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'e.g. 101'
            }),
            'room_type': forms.Select(attrs={
                'class': 'form-input'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-input',
                'placeholder': 'e.g. 1500.00',
                'step': '0.01'
            }),
            'floor': forms.NumberInput(attrs={
                'class': 'form-input',
                'placeholder': 'e.g. 1'
            }),
            'availability': forms.CheckboxInput(attrs={
                'class': 'form-checkbox'
            }),
        }
