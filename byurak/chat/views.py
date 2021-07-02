from django.shortcuts import render

from chat.models import ChattingRoom
from chat.models import Message

def index_3(request):
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

    return render(request, 'index3.html', {
        'chat_room': chat_room_index, 
        'chat_member': chat_room_member,
        'chat_room_all': chat_room
        }
        )


def room(request, room_name):
    messages = Message.objects.filter(object_id=int(room_name))

    return render(request, 'room.html', {'room_name': room_name,  'messages':messages, 'request_user':request.user})


def test(request):
    return render(request, 'test.html')
