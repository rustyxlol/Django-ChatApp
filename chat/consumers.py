import json
from asgiref.sync import sync_to_async

from channels.auth import login, logout
from channels.generic.websocket import AsyncWebsocketConsumer

from . models import Message


class ChatConsumer(AsyncWebsocketConsumer):
    """
    A consumer does three things:
    1. Accepts connections.
    2. Receives messages from client.
    3. Disconnects when the job is done.
    """

    async def connect(self):
        """
        Connect to a room
        """
        # Connect only if the user is authenticated
        user = self.scope['user']

        if user.is_authenticated:
            self.room_name = self.scope['url_route']['kwargs']['room_name']
            # self.room_group_name = 'chat_%s' % self.room_name
            self.room_group_name = f"chat_{self.room_name}"

            # Join room group
            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )
            await self.accept()

        else:
            await self.send({"close": True})

    async def disconnect(self, close_code):
        """
        Disconnect from channel

        :param close_code: optional
        """
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        """
        Receive messages from WebSocket

        :param text_data: message
        """

        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = text_data_json['username']
        profile_pic = text_data_json['profile_pic']
        room = text_data_json['room']

        # Save message to DB
        await self.save_message(message, username, profile_pic, room)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username,
                'profile_pic': profile_pic,
                'room': room,
            }
        )

    async def chat_message(self, event):
        """
        Receive messages from room group

        :param event: Events to pick up
        """
        message = event['message']
        username = event['username']
        profile_pic = event['profile_pic']
        room = event['room']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'profile_pic': profile_pic,
            'room': room,
        }))

    @sync_to_async
    def save_message(self, message, username, profile_pic, room):
        Message.objects.create(
            message_content=message, username=username, profile_pic=profile_pic, room=room)
