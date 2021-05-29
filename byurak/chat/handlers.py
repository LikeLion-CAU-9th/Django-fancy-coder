import abc

from channels.exceptions import StopConsumer
from chat.models import Message


class BaseEventHandler:

    class Meta:
        abstract = True

    def __init__(self, consumer):
        self._consumer = consumer

    def get_handler(self, event):
        return getattr(self, f'on_{event}', None)

    async def check_key(self, event, data, *keys):
        """
        :param keys: data valid key
        :param event: event name str
        :param data: dict{key: value}
        """
        for key in keys:
            if key not in data:
                await self._consumer.to_error(
                    code=4000,
                    event_type=event,
                    message=f"Data must contain {key}",
                )
                raise StopConsumer


class ChatEventHandler(BaseEventHandler):

    class Meta:
        abstract = True

    @abc.abstractmethod
    async def get_messages_on_enter(self):
        pass

    # async def get_messages(self, reverse, paging, *args, **kwargs):
    #     queryset = self._consumer.room.get_messages(paging=paging, reverse=reverse, *args, **kwargs)
    #     messages = await async_serialized(MessageSerializer, queryset)
    #     return messages

    async def filter_messages(self, *, direction, cursor, paging):
        filter_args = {'created_at__lt': cursor} if direction == 'previous' else {'created_at__gt': cursor}
        messages = await self.get_messages(
            reverse=direction == 'next',
            paging=paging,
            **filter_args
        )
        if direction == 'previous':
            messages.reverse()
        return messages

    async def get_messages_with_read_at(self):
        previous_msg = await self.get_messages(reverse=False, paging=True, created_at__lte=self._consumer.read_at)
        if previous_msg:
            previous_msg.reverse()
        next_msg = await self.get_messages(reverse=True, paging=True, created_at__gt=self._consumer.read_at)
        if previous_msg and next_msg:
            previous_msg.append(Message.get_read_point_message())
        return previous_msg + next_msg

    async def send_message(self, content):
        await Message.objects.async_create(
            user_id=self._consumer.user_id,
            content_object=self._consumer.room,
            content=content
        )
        # await self._consumer.group_send(
        #     subject_type='message',
        #     event_type='message',
        #     data=MessageSerializer(instance).data,
        # )
