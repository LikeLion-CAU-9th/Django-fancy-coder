from django.contrib import admin
from chat.models import Message, ChattingRoom


admin.site.register(Message)
admin.site.register(ChattingRoom)