from django import forms


class RoomForm(forms.Form):
    room_name = forms.CharField()
