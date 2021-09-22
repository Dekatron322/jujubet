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
        fields = (
                    'home_team', 'away_team', 'league', 'tip', 'odds', 
                    'a_home_team', 'a_away_team', 'a_league', 'a_tip', 'a_odds',
                    'b_home_team', 'b_away_team', 'b_league', 'b_tip', 'b_odds',
                    'c_home_team', 'c_away_team', 'c_league', 'c_tip', 'c_odds',
                    'd_home_team', 'd_away_team', 'd_league', 'd_tip', 'd_odds',
                    ##
                    'dA_home_team', 'dA_away_team', 'dA_league', 'dA_tip', 'dA_odds', 
                    'dB_home_team', 'dB_away_team', 'dB_league', 'dB_tip', 'dB_odds',
                    'tA_home_team', 'tA_away_team', 'tA_league', 'tA_tip', 'tA_odds', 
                    'tB_home_team', 'tB_away_team', 'tB_league', 'tB_tip', 'tB_odds',
                    'tC_home_team', 'tC_away_team', 'tC_league', 'tC_tip', 'tC_odds',
                    'fA_home_team', 'fA_away_team', 'fA_league', 'fA_tip', 'fA_odds', 
                    'fB_home_team', 'fB_away_team', 'fB_league', 'fB_tip', 'fB_odds',
                    'fC_home_team', 'fC_away_team', 'fC_league', 'fC_tip', 'fC_odds',
                    'fD_home_team', 'fD_away_team', 'fD_league', 'fD_tip', 'fD_odds',
                    ## five
                    'ffA_home_team', 'ffA_away_team', 'ffA_league', 'ffA_tip', 'ffA_odds',
                    'ffB_home_team', 'ffB_away_team', 'ffB_league', 'ffB_tip', 'ffB_odds', 
                    'ffC_home_team', 'ffC_away_team', 'ffC_league', 'ffC_tip', 'ffC_odds',
                    'ffD_home_team', 'ffD_away_team', 'ffD_league', 'ffD_tip', 'ffD_odds',
                    'ffE_home_team', 'ffE_away_team', 'ffE_league', 'ffE_tip', 'ffE_odds',
                    ## six
                    'siA_home_team', 'siA_away_team', 'siA_league', 'siA_tip', 'siA_odds',
                    'siB_home_team', 'siB_away_team', 'siB_league', 'siB_tip', 'siB_odds', 
                    'siC_home_team', 'siC_away_team', 'siC_league', 'siC_tip', 'siC_odds',
                    'siD_home_team', 'siD_away_team', 'siD_league', 'siD_tip', 'siD_odds',
                    'siE_home_team', 'siE_away_team', 'siE_league', 'siE_tip', 'siE_odds',
                    'siF_home_team', 'siF_away_team', 'siF_league', 'siF_tip', 'siF_odds',
                    ##seven
                    'sA_home_team', 'sA_away_team', 'sA_league', 'sA_tip', 'sA_odds',
                    'sB_home_team', 'sB_away_team', 'sB_league', 'sB_tip', 'sB_odds', 
                    'sC_home_team', 'sC_away_team', 'sC_league', 'sC_tip', 'sC_odds',
                    'sD_home_team', 'sD_away_team', 'sD_league', 'sD_tip', 'sD_odds',
                    'sE_home_team', 'sE_away_team', 'sE_league', 'sE_tip', 'sE_odds',
                    'sF_home_team', 'sF_away_team', 'sF_league', 'sF_tip', 'sF_odds',
                    'gF_home_team', 'gF_away_team', 'gF_league', 'gF_tip', 'gF_odds',
                    ## corect score
                    'ccA_home_team', 'ccA_away_team', 'ccA_league', 'ccA_tip', 'ccA_odds',
                    'ccB_home_team', 'ccB_away_team', 'ccB_league', 'ccB_tip', 'ccB_odds', 
                    'ccC_home_team', 'ccC_away_team', 'ccC_league', 'ccC_tip', 'ccC_odds',
                    'ccD_home_team', 'ccD_away_team', 'ccD_league', 'ccD_tip', 'ccD_odds',
                    'ccE_home_team', 'ccE_away_team', 'ccE_league', 'ccE_tip', 'ccE_odds',
                    'ccF_home_team', 'ccF_away_team', 'ccF_league', 'ccF_tip', 'ccF_odds',
                    'ccG_home_team', 'ccG_away_team', 'ccG_league', 'ccG_tip', 'ccG_odds',
                    'ccH_home_team', 'ccH_away_team', 'ccH_league', 'ccH_tip', 'ccH_odds', 
                    'ccI_home_team', 'ccI_away_team', 'ccI_league', 'ccI_tip', 'ccI_odds',
                    'ccJ_home_team', 'ccJ_away_team', 'ccJ_league', 'ccJ_tip', 'ccJ_odds',
                    ## goal goal
                    'ggA_home_team', 'ggA_away_team', 'ggA_league', 'ggA_tip', 'ggA_odds',
                    'ggB_home_team', 'ggB_away_team', 'ggB_league', 'ggB_tip', 'ggB_odds', 
                    'ggC_home_team', 'ggC_away_team', 'ggC_league', 'ggC_tip', 'ggC_odds',
                    'ggD_home_team', 'ggD_away_team', 'ggD_league', 'ggD_tip', 'ggD_odds',
                    'ggE_home_team', 'ggE_away_team', 'ggE_league', 'ggE_tip', 'ggE_odds',
                    'ggF_home_team', 'ggF_away_team', 'ggF_league', 'ggF_tip', 'ggF_odds',
                    'ggG_home_team', 'ggG_away_team', 'ggG_league', 'ggG_tip', 'ggG_odds',
                    'ggH_home_team', 'ggH_away_team', 'ggH_league', 'ggH_tip', 'ggH_odds', 
                    'ggI_home_team', 'ggI_away_team', 'ggI_league', 'ggI_tip', 'ggI_odds',
                    'ggJ_home_team', 'ggJ_away_team', 'ggJ_league', 'ggJ_tip', 'ggJ_odds',
                    ## half time
                    'htA_home_team', 'htA_away_team', 'htA_league', 'htA_tip', 'htA_odds',
                    'htB_home_team', 'htB_away_team', 'htB_league', 'htB_tip', 'htB_odds', 
                    'htC_home_team', 'htC_away_team', 'htC_league', 'htC_tip', 'htC_odds',
                    'htD_home_team', 'htD_away_team', 'htD_league', 'htD_tip', 'htD_odds',
                    'htE_home_team', 'htE_away_team', 'htE_league', 'htE_tip', 'htE_odds',
                    'htF_home_team', 'htF_away_team', 'htF_league', 'htF_tip', 'htF_odds',
                    'htG_home_team', 'htG_away_team', 'htG_league', 'htG_tip', 'htG_odds',
                    'htH_home_team', 'htH_away_team', 'htH_league', 'htH_tip', 'htH_odds', 
                    'htI_home_team', 'htI_away_team', 'htI_league', 'htI_tip', 'htI_odds',
                    'htJ_home_team', 'htJ_away_team', 'htJ_league', 'htJ_tip', 'htJ_odds',
                    ##full time
                    'ftA_home_team', 'ftA_away_team', 'ftA_league', 'ftA_tip', 'ftA_odds',
                    'ftB_home_team', 'ftB_away_team', 'ftB_league', 'ftB_tip', 'ftB_odds', 
                    'ftC_home_team', 'ftC_away_team', 'ftC_league', 'ftC_tip', 'ftC_odds',
                    'ftD_home_team', 'ftD_away_team', 'ftD_league', 'ftD_tip', 'ftD_odds',
                    'ftE_home_team', 'ftE_away_team', 'ftE_league', 'ftE_tip', 'ftE_odds',
                    'ftF_home_team', 'ftF_away_team', 'ftF_league', 'ftF_tip', 'ftF_odds',
                    'ftG_home_team', 'ftG_away_team', 'ftG_league', 'ftG_tip', 'ftG_odds',
                    'ftH_home_team', 'ftH_away_team', 'ftH_league', 'ftH_tip', 'ftH_odds', 
                    'ftI_home_team', 'ftI_away_team', 'ftI_league', 'ftI_tip', 'ftI_odds',
                    'ftJ_home_team', 'ftJ_away_team', 'ftJ_league', 'ftJ_tip', 'ftJ_odds',
                    )



class MatchForm(FormSettings):

    def __init__(self, *args, **kwargs):
        super(MatchForm, self).__init__(*args, **kwargs)

    class Meta:
        model = VipGames
        fields = '__all__'

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