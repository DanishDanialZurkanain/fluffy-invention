from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Room, User

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = [
            'topic',
            'name',
            'description',
        ]

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'image'
        ]

class UserRegisterForm(UserCreationForm ):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]