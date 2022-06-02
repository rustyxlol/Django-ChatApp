from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RoomForm
# from .models import Room - used context processor instead


@login_required()
def chat_home(request):

    form = RoomForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        room_name = form.cleaned_data['room_name']
        messages.success(request, f"Found: {room_name}")
        return render(request, 'chat/chatroom.html', {'room_name': room_name, 'title': room_name})

    return render(request, 'chat/index.html', {'form': form})


@login_required
def chat_room(request, room_name):
    return render(request, 'chat/chatroom.html', {
        'room_name': room_name,
        'title': room_name,
    })
