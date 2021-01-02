from django.shortcuts import render
from .models import Room
from .serializers import RoomSerializer, UpdateRoomSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
<<<<<<< HEAD
<<<<<<< HEAD
from django.http import JsonResponse
=======
<<<<<<< HEAD
=======
from django.http import JsonResponse
>>>>>>> c6e2a7fd... added spotify api
>>>>>>> 9ae9138d... added spotify api
=======
from django.http import JsonResponse
>>>>>>> 6d3401ba... updated views and urls


# Create your views here.


class RoomView(APIView):
    """
    List all rooms, or create a new room.
    """

    def get(self, request, format=None):
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            guest_can_pause = serializer.data.get('guest_can_pause')
            votes_to_skip = serializer.data.get('votes_to_skip')
            host = self.request.session.session_key
            queryset = Room.objects.filter(host=host)
            if queryset.exists():
                room = queryset[0]
                room.guest_can_pause = guest_can_pause
                room.votes_to_skip = votes_to_skip
                room.save(update_fields=['guest_can_pause', 'votes_to_skip'])
                serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


<<<<<<< HEAD
<<<<<<< HEAD
class GetRoom(APIView):
=======
<<<<<<< HEAD
class UpdateRoom(APIView):
>>>>>>> 9ae9138d... added spotify api
    """
    Retrieve a room.
    """

    lookup_url_kwarg = 'code'
    serializer_class = RoomSerializer

<<<<<<< HEAD
=======
    def delete(self, request, pk, format=None):
        room = self.get_object(pk)
        room.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
=======
=======
>>>>>>> 6d3401ba... updated views and urls
class GetRoom(APIView):
    """
    Retrieve a room.
    """

    serializer_class = RoomSerializer
    lookup_url_kwarg = 'code'

<<<<<<< HEAD
>>>>>>> 9ae9138d... added spotify api
    def get(self,request, format=None):
=======
    def get(self, request, format=None):
>>>>>>> 6d3401ba... updated views and urls
        code = request.GET.get(self.lookup_url_kwarg)
        if code != None:
            room = Room.objects.filter(code=code)
            if len(room) > 0:
                data = RoomSerializer(room[0]).data
                data['is_host'] = self.request.session.session_key == room[0].host
                return Response(data, status=status.HTTP_200_OK)
            return Response({'Room Not Found': 'Invalid Room Code.'}, status=status.HTTP_404_NOT_FOUND)
<<<<<<< HEAD
        
        return Response({'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
<<<<<<< HEAD
=======
>>>>>>> c6e2a7fd... added spotify api
>>>>>>> 9ae9138d... added spotify api
=======

        return Response({'Bad Request': 'Code paramater not found in request'}, status=status.HTTP_400_BAD_REQUEST)
>>>>>>> 6d3401ba... updated views and urls


class JoinRoom(APIView):
    """
    Join a room.
    """
<<<<<<< HEAD
<<<<<<< HEAD

=======
<<<<<<< HEAD
=======

>>>>>>> c6e2a7fd... added spotify api
>>>>>>> 9ae9138d... added spotify api
=======
>>>>>>> 6d3401ba... updated views and urls
    lookup_url_kwarg = 'code'

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        code = request.data.get(self.lookup_url_kwarg)
        if code != None:
            room_result = Room.objects.filter(code=code)
            if len(room_result) > 0:
                room = room_result[0]
                self.request.session['room_code'] = code
                return Response({'message': 'Room Joined!'}, status=status.HTTP_200_OK)

            return Response({'Bad Request': 'Invalid Room Code'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'Bad Request': 'Invalid post data, did not find a code key'}, status=status.HTTP_400_BAD_REQUEST)


class LeaveRoom(APIView):
    """
    Leave a room in progress.
    """
    def post(self, request, format=None):
        if 'room_code' in self.request.session:
            self.request.session.pop('room_code')
            host_id = self.request.session.session_key
            room_results = Room.objects.filter(host=host_id)
            if len(room_results) > 0:
                room = room_results[0]
                room.delete()
        return Response({'Message': 'Success'}, status=status.HTTP_200_OK)
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> 9ae9138d... added spotify api
=======
>>>>>>> 6d3401ba... updated views and urls


class UserInRoom(APIView):
    """
    Checks if user is in room.
    """
    def get(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        data = {
            'code': self.request.session.get('room_code')
        }
        return JsonResponse(data, status=status.HTTP_200_OK)

class UpdateRoom(APIView):
    serializer_class = UpdateRoomSerializer

    def patch(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            guest_can_pause = serializer.data.get('guest_can_pause')
            votes_to_skip = serializer.data.get('votes_to_skip')
            code = serializer.data.get('code')

            queryset = Room.objects.filter(code=code)
            if not queryset.exists():
                return Response({'msg': 'Room not found.'}, status=status.HTTP_404_NOT_FOUND)

            room = queryset[0]
            user_id = self.request.session.session_key
            if room.host != user_id:
                return Response({'msg': 'You are not the host of this room.'}, status=status.HTTP_403_FORBIDDEN)

            room.guest_can_pause = guest_can_pause
            room.votes_to_skip = votes_to_skip
            room.save(update_fields=['guest_can_pause', 'votes_to_skip'])
            return Response(RoomSerializer(room).data, status=status.HTTP_200_OK)

        return Response({'Bad Request': "Invalid Data..."}, status=status.HTTP_400_BAD_REQUEST)
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> c6e2a7fd... added spotify api
>>>>>>> 9ae9138d... added spotify api
=======
>>>>>>> 6d3401ba... updated views and urls
