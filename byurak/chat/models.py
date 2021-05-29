import uuid

from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.auth.models import User
from channels.db import database_sync_to_async

from chat.managers import MessageManager


"""

Model Logic
1. BaseChatModel : to save
2. ChatModel 
3. RoomModel

"""


class BaseChatModel(models.Model):
    @database_sync_to_async
    def async_save(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.save(update_fields=kwargs.keys())

    class Meta:
        abstract = True


class ChattingModel(BaseChatModel):
    message_size = 30
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Message(ChattingModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    object_id = models.PositiveIntegerField(verbose_name='채팅방 아이디')
    user_id = models.PositiveIntegerField(db_index=True, verbose_name='유저 아이디')
    content = models.TextField(verbose_name='내용')

    objects = MessageManager()

    class Meta:
        ordering = ('-created_at',)
        indexes = [
            models.Index(fields=['-created_at'])
        ]


class Room(ChattingModel):
    messages = GenericRelation('chat.Message')

    class Meta:
        abstract = True

    def get_messages(self, *args, reverse=False, paging=True, **kwargs):
        filtered_messages = self.messages.filter(*args, **kwargs)
        if reverse:
            filtered_messages = filtered_messages.order_by('created_at')
        if not paging:
            return filtered_messages
        return filtered_messages[:self.message_size]

    def get_all_messages(self):
        return list(
            self.messages.values(
                'object_id',
                'user_id',
                'content',
                'type',
            )
        )


class ChattingRoom(Room):
    chat_id = models.PositiveIntegerField(
        verbose_name='채팅방 id', primary_key=False)
    created_at = models.DateTimeField(verbose_name='채팅방이 생성된 날짜')
    room = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='member')

    @property
    def members_list(self):
        return self.group.values_list('user_id', flat=True)
