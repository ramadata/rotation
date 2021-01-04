from django.contrib import admin
from django.urls import path
from .views import RoomView, CreatRoomView, GetRoom, JoinRoom, LeaveRoom, UpdateRoom, UserInRoom



urlpatterns = [
    path('room', RoomView.as_view()),
    path('create-room', CreatRoomView.as_view()),
    path('get-room', GetRoom.as_view()),
    path('join-room', JoinRoom.as_view()),
    path('leave-room', LeaveRoom.as_view()),
    path('update-room', UpdateRoom.as_view()),
    path('user-in-room', UserInRoom.as_view()),
]
