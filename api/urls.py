from django.urls import path
from .views import UserListView, UserDetailView, RoomListView, RoomDetailView, CreateRoomView

app_name = 'api'

urlpatterns = [
    path('user-list', UserListView.as_view(), name='user-list'),
    path('user-detail', UserDetailView.as_view(), name='user-detail'),
    path('room-list', RoomListView.as_view(), name='room-list'),
    path('room-detail', RoomDetailView.as_view(), name='room-detail'),
    path('create-room', CreateRoomView.as_view(), name='create-room'),
]