from channels.db import database_sync_to_async
from django.db.models.manager import BaseManager

from chat.queryset import DefaultQuerySet


class DefaultManager(BaseManager.from_queryset(DefaultQuerySet)):
    @database_sync_to_async
    def async_get(self, **kwargs):
        return self.get(**kwargs)


class MessageManager(DefaultManager):

    @database_sync_to_async
    def async_create(self, user_id, content, **kwargs):
        """
        :param(*required)
            user_id: self.scope['user'].user_id
            content_object: self.scope['room']
            type: Message.MessageType
            content: str message content
        """
        return self.create(
            user_id=user_id,
            content=content,
            **kwargs
        )

