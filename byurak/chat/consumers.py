import datetime
import json

from asgiref.sync import async_to_sync, sync_to_async
from channels.db import database_sync_to_async
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from django.contrib.auth.models import User

from chat.handlers import ChatEventHandler
from chat.models import Message, ChattingRoom


class ChatConsumer(AsyncWebsocketConsumer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.event_handler = ChatEventHandler(self)

    @property
    def user(self):
        return self.scope['user']

    @property
    def room(self):
        return self.scope['url_route']['kwargs']['room_name']

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        self.username = await database_sync_to_async(self.get_name)()
        user = self.scope['user'].username
        username = await sync_to_async(self.get_user)(user)

        await sync_to_async(self.create_chat_room)(self.room_name, username)

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name,
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name,
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print(text_data_json)
        chatroom_id = self.scope['url_route']['kwargs']['room_name']
        self.username = await database_sync_to_async(self.get_name)()

        user = self.scope["user"].username
        username = await sync_to_async(self.get_user)(user)
        print(username.id)

        await Message.objects.async_create(
            object_id=chatroom_id,
            user_id=username.id,
            content=message
        )

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'user': user,
                'username': self.username,
                'chat_room': chatroom_id
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        user = event['user']
        self.username = await database_sync_to_async(self.get_name)()
        print(event)

        print(self.event_handler.send_message(message))

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'user': user
        }))

    def get_name(self):
        return User.objects.all()[0].username

    def get_user(self, username):
        return User.objects.get(username=username)

    def create_chat_room(self, chat_room_id, user):
        is_chat = ChattingRoom.objects.filter(
            chat_id=int(chat_room_id),
            room=user
        )
        if not is_chat:
            return ChattingRoom.objects.create(
                chat_id=int(chat_room_id),
                room=user,
                created_at=datetime.datetime.now()
            )
        return

    # def get_name(self):
    #     return User.objects.get(username="oereo").username
    #     # return self.get_user
    #
    # def get_user(self, request):
    #     print(request.user.username)
    #     return request.user.username


"""
동기식으로 ChatConsumer를 구현할 경우
"""
# class ChatConsumer(WebsocketConsumer):
#     def connect(self):
#         """
#         room_name : parameter from URL route websocket connection to the consumer
#
#         async def connect(self):
#            await self.channel_layer.group_add(
#               self.room.group_channel_name,
#               self.channel_name
#            )
#            await self.accept()
#         -> 아래 코드와 위 코드의 차이는??? synchronous 한지 asynchronous 인지 의 차이가 아닐까...!
#         :return:
#         """
#         self.room_name = self.scope['url_route']['kwargs']['room_name']
#         self.room_group_name = 'chat_%s' % self.room_name
#
#         # Join room group
#         async_to_sync(self.channel_layer.group_add)(
#             self.room_group_name,
#             self.channel_name
#         )
#
#         self.accept()
#
#     def disconnect(self, close_code):
#         # Leave room group
#         async_to_sync(self.channel_layer.group_discard)(
#             self.room_group_name,
#             self.channel_name
#         )
#
#     # Receive message from WebSocket
#     def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json['message']
#
#         # Send message to room group
#         async_to_sync(self.channel_layer.group_send)(
#             self.room_group_name,
#             {
#                 'type': 'chat_message',
#                 'message': message
#             }
#         )
#
#     # Receive message from room group
#     def chat_message(self, event):
#         message = event['message']
#
#         # Send message to WebSocket
#         self.send(text_data=json.dumps({
#             'message': message
#         }))
