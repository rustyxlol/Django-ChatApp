"""
Crispy form for entering a room name
"""
from django import forms


class RoomForm(forms.Form):
    """
    Normal form, not connected to models.
    """
    room_name = forms.CharField()
