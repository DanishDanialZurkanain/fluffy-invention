from typing import List
from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView
from base.models import Room

from .serializers import UserSerializer, RoomSerializer, CreateRoomSerializer

# Create your views here.
class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(ListAPIView):
    def get_queryset(self):
        queryset = User.objects.filter(username=self.request.user)
        return queryset

    serializer_class = UserSerializer

class RoomListView(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class RoomDetailView(ListAPIView):
    def get_queryset(self):
        queryset = Room.objects.filter(host=self.request.user)
        return queryset

    serializer_class = RoomSerializer

class CreateRoomView(CreateAPIView):
    def get_queryset(self):
        query_set = Room.objects.all()
        return query_set

    serializer_class = CreateRoomSerializer

class DeleteRoomView(DestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer