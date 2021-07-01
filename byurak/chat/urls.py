from django.urls import path
import chat.views

urlpatterns = [
    path('te', chat.views.index_3, name='index3'),
    path('<str:room_name>/', chat.views.room, name='room'),
    path('test', chat.views.test, name="test")
]