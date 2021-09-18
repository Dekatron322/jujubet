from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, Select, FileInput
from .models import *


class FormSettings(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormSettings, self).__init__(*args, **kwargs)

        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

class SignUpForm(UserCreationForm):
	username = forms.CharField(max_length=30, label= 'User Name :')
	email = forms.EmailField(max_length=200, label= 'Email :')
	first_name = forms.CharField(max_length=100, help_text='First Name', label= 'First Name :')
	last_name = forms.CharField(max_length=100, help_text='Last Name', label= 'Last Name :')

	class Meta:
		model = User
		fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')



class MessageForm(FormSettings):

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Message
        fields = ['title', 'message']

class GamesForm(FormSettings):

    def __init__(self, *args, **kwargs):
        super(GamesForm, self).__init__(*args, **kwargs)

    class Meta:
        model = VipGames
        fields = ('home_team', 'away_team', 'league', 'tip', 'odds')


class MatchForm(FormSettings):

    def __init__(self, *args, **kwargs):
        super(MatchForm, self).__init__(*args, **kwargs)

    class Meta:
        model = VipGames
        fields = ('home_team', 'away_team', 'league', 'tip', 'odds', 'result')

class AdvertForm(FormSettings):

    def __init__(self, *args, **kwargs):
        super(AdvertForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Advert
        fields = ('title', 'link', 'image')



class AdvertUpdateForm(FormSettings):
    class Meta:
        model = Advert
        fields = ['title','link', 'image']