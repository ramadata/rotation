from django.contrib import admin
from django.urls import path
<<<<<<< HEAD
<<<<<<< HEAD
from .views import RoomView, GetRoom, JoinRoom, LeaveRoom, UserInRoom, UpdateRoom
=======
<<<<<<< HEAD
from .views import RoomView, UpdateRoom, JoinRoom, LeaveRoom
=======
from .views import RoomView, GetRoom, JoinRoom, LeaveRoom, UserInRoom, UpdateRoom
>>>>>>> c6e2a7fd... added spotify api
>>>>>>> 9ae9138d... added spotify api
=======
from .views import RoomView, GetRoom, JoinRoom, LeaveRoom, UserInRoom, UpdateRoom
>>>>>>> 6d3401ba... updated views and urls
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('room', RoomView.as_view()),
<<<<<<< HEAD
<<<<<<< HEAD
    path('get-room', GetRoom.as_view()),
    path('join', JoinRoom.as_view()),
    path('leave', LeaveRoom.as_view()),
    path('user', UserInRoom.as_view()),
    path('update', UpdateRoom.as_view()),
] 
=======
<<<<<<< HEAD
    path('update', UpdateRoom.as_view()),
    path('join', JoinRoom.as_view()),
    path('leave', LeaveRoom.as_view()),
]
=======
=======
>>>>>>> 6d3401ba... updated views and urls
    path('get-room', GetRoom.as_view()),
    path('join-room', JoinRoom.as_view()),
    path('leave-room', LeaveRoom.as_view()),
    path('user-in-room', UserInRoom.as_view()),
    path('update', UpdateRoom.as_view()),
] 
<<<<<<< HEAD
>>>>>>> c6e2a7fd... added spotify api
>>>>>>> 9ae9138d... added spotify api
=======
>>>>>>> 6d3401ba... updated views and urls
