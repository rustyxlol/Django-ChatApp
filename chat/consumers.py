import json
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    """
    A consumer does three things:
    1. Accepts connections.
    2. Receives messages from client.
    3. Disconnects when the job is done.
    """
    # A consumer does three things
    # Accepts connections
    # Disconnect
    # Receive messages from client

    def connect(self):
        self.accept()

    def disconnect():
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        self.send(text_data=json.dumps({
            'message': message
        }))
