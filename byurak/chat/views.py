from django.shortcuts import render

from chat.models import ChattingRoom


def index(request):
    chat_room = ChattingRoom.objects.all()
    chat_room_index = {}
    chat_room_member = {}
    for index in range(0, chat_room.count()):
        chat_room_no = chat_room[index].chat_id
        chat_room_mem = chat_room[index].room
        try:
            chat_room_index[chat_room_no] += 1
            chat_room_member[chat_room_no] += chat_room_mem
        except:
            chat_room_index[chat_room_no] = 1

    return render(request, 'index.html', {'chat_room': chat_room_index, 'chat_member': chat_room_member})


def room(request, room_name):
    return render(request, 'room.html', {'room_name': room_name})
