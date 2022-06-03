from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import RoomForm
from .models import Message, Room


@login_required()
def chat_home(request):

    form = RoomForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        room_name = form.cleaned_data['room_name']
        db_messages = Message.objects.filter(room=room_name)[:]
        messages.success(request, f"Joined: {room_name}")
        return render(request, 'chat/chatroom.html', {'room_name': room_name, 'title': room_name, 'db_messages': db_messages})

    return render(request, 'chat/index.html', {'form': form})


@login_required
def chat_room(request, room_name):
    db_messages = Message.objects.filter(room=room_name)[:]

    messages.success(request, f"Joined: {room_name}")
    return render(request, 'chat/chatroom.html', {
        'room_name': room_name,
        'title': room_name,
        'db_messages': db_messages,
    })
