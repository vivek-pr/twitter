from django import forms
from django.contrib.auth.models import User
from .models import Tweets
from django.contrib.auth.forms import UserChangeForm

class UserForm(forms.ModelForm):
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = (
            'username',
            'password',
        )


class TweetForm(forms.ModelForm):
    class Meta:
        model=Tweets
        fields=(
            'text',

            )
