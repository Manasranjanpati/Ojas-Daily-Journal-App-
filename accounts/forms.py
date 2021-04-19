
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import OjasCustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = OjasCustomUser
        fields = ('first_name','last_name','username', 'email', 'age','location','phonenumber') 


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = OjasCustomUser
        fields = ('username', 'email', 'age',)
