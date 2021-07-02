from django.urls import path
import chat.views

urlpatterns = [
    path('', chat.views.index_3, name='chat-index'),
    path('<str:room_name>/', chat.views.room, name='room'),
    path('test', chat.views.test, name="test")
]