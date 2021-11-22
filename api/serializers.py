from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from base.models import Room

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username', 
            'email', 
            'first_name', 
            'last_name'
        ]

class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class CreateRoomSerializer(ModelSerializer):
    host = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Room
        fields = [
            'name',
            'description',
            'topic',
            'host'
        ]