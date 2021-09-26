from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm, Textarea, TextInput, Select
from django.utils import timezone


# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	phone = models.CharField(blank=True, max_length=20)
	address = models.CharField(blank=True, max_length=150)
	city = models.CharField(blank=True, max_length=20)
	image = models.ImageField(blank=True)

	def __str__(self):
		return self.user.username

	def user_name(self):
		return self.user.first_name + '' + self.user.last_name + '[' + self.user.username + ']'



class Message(models.Model):
	title = models.CharField(blank=True, max_length=100)
	message = models.TextField()
	#user = models.OneToOneField(User, on_delete=models.CASCADE)
	create_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.title

class Advert(models.Model):
	title = models.CharField(blank=True, max_length=100)
	link = models.CharField(blank=True, max_length=1000)
	image = models.ImageField(upload_to='media', blank=True)

class VipGames(models.Model):
	RESULT = [("WON", "WON"), ("LOST", "LOST"), ("PENDING", "PENDING")]
	## single prediction 
	home_team = models.CharField(blank=True, max_length=100, default="None")
	away_team = models.CharField(blank=True, max_length=100, default="None")
	league = models.CharField(max_length=1000, blank=True , default="None")
	tip = models. CharField(blank=True, max_length=20, default="None")
	odds = models.CharField(blank=True, max_length=20, default="None")
	result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_1 = models.IntegerField(default=0)

	a_home_team = models.CharField(blank=True, max_length=100, default="None")
	a_away_team = models.CharField(blank=True, max_length=100, default="None")
	a_league = models.CharField(max_length=1000, blank=True , default="None")
	a_tip = models. CharField(blank=True, max_length=20, default="None")
	a_odds = models.CharField(blank=True, max_length=20, default="None")
	a_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_2 = models.IntegerField(default=0)

	b_home_team = models.CharField(blank=True, max_length=100, default="None")
	b_away_team = models.CharField(blank=True, max_length=100, default="None")
	b_league = models.CharField(max_length=1000, blank=True , default="None")
	b_tip = models. CharField(blank=True, max_length=20, default="None")
	b_odds = models.CharField(blank=True, max_length=20, default="None")
	b_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_3 = models.IntegerField(default=0)

	c_home_team = models.CharField(blank=True, max_length=100, default="None")
	c_away_team = models.CharField(blank=True, max_length=100, default="None")
	c_league = models.CharField(max_length=1000, blank=True , default="None")
	c_tip = models. CharField(blank=True, max_length=20, default="None")
	c_odds = models.CharField(blank=True, max_length=20, default="None")
	c_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_4 = models.IntegerField(default=0)

	d_home_team = models.CharField(blank=True, max_length=100, default="None")
	d_away_team = models.CharField(blank=True, max_length=100, default="None")
	d_league = models.CharField(max_length=1000, blank=True , default="None")
	d_tip = models. CharField(blank=True, max_length=20, default="None")
	d_odds = models.CharField(blank=True, max_length=20, default="None")
	d_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_5 = models.IntegerField(default=0)


	## prediction double 

	dA_home_team = models.CharField(blank=True, max_length=100, default="None")
	dA_away_team = models.CharField(blank=True, max_length=100, default="None")
	dA_league = models.CharField(max_length=1000, blank=True , default="None")
	dA_tip = models. CharField(blank=True, max_length=20, default="None")
	dA_odds = models.CharField(blank=True, max_length=20, default="None")
	dA_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_6 = models.IntegerField(default=0)

	dB_home_team = models.CharField(blank=True, max_length=100, default="None")
	dB_away_team = models.CharField(blank=True, max_length=100, default="None")
	dB_league = models.CharField(max_length=1000, blank=True , default="None")
	dB_tip = models. CharField(blank=True, max_length=20, default="None")
	dB_odds = models.CharField(blank=True, max_length=20, default="None")
	dB_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_7 = models.IntegerField(default=0)


	## prediction multiple 1/3

	tA_home_team = models.CharField(blank=True, max_length=100, default="None")
	tA_away_team = models.CharField(blank=True, max_length=100, default="None")
	tA_league = models.CharField(max_length=1000, blank=True , default="None")
	tA_tip = models. CharField(blank=True, max_length=20, default="None")
	tA_odds = models.CharField(blank=True, max_length=20, default="None")
	tA_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_8 = models.IntegerField(default=0)

	tB_home_team = models.CharField(blank=True, max_length=100, default="None")
	tB_away_team = models.CharField(blank=True, max_length=100, default="None")
	tB_league = models.CharField(max_length=1000, blank=True , default="None")
	tB_tip = models. CharField(blank=True, max_length=20, default="None")
	tB_odds = models.CharField(blank=True, max_length=20, default="None")
	tB_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_9 = models.IntegerField(default=0)

	tC_home_team = models.CharField(blank=True, max_length=100, default="None")
	tC_away_team = models.CharField(blank=True, max_length=100, default="None")
	tC_league = models.CharField(max_length=1000, blank=True , default="None")
	tC_tip = models. CharField(blank=True, max_length=20, default="None")
	tC_odds = models.CharField(blank=True, max_length=20, default="None")
	tC_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_10 = models.IntegerField(default=0)


	## prediction multiple 1/4

	fA_home_team = models.CharField(blank=True, max_length=100, default="None")
	fA_away_team = models.CharField(blank=True, max_length=100, default="None")
	fA_league = models.CharField(max_length=1000, blank=True , default="None")
	fA_tip = models. CharField(blank=True, max_length=20, default="None")
	fA_odds = models.CharField(blank=True, max_length=20, default="None")
	fA_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_11 = models.IntegerField(default=0)

	fB_home_team = models.CharField(blank=True, max_length=100, default="None")
	fB_away_team = models.CharField(blank=True, max_length=100, default="None")
	fB_league = models.CharField(max_length=1000, blank=True , default="None")
	fB_tip = models. CharField(blank=True, max_length=20, default="None")
	fB_odds = models.CharField(blank=True, max_length=20, default="None")
	fB_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_12 = models.IntegerField(default=0)

	fC_home_team = models.CharField(blank=True, max_length=100, default="None")
	fC_away_team = models.CharField(blank=True, max_length=100, default="None")
	fC_league = models.CharField(max_length=1000, blank=True , default="None")
	fC_tip = models. CharField(blank=True, max_length=20, default="None")
	fC_odds = models.CharField(blank=True, max_length=20, default="None")
	fC_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_13 = models.IntegerField(default=0)

	fD_home_team = models.CharField(blank=True, max_length=100, default="None")
	fD_away_team = models.CharField(blank=True, max_length=100, default="None")
	fD_league = models.CharField(max_length=1000, blank=True , default="None")
	fD_tip = models. CharField(blank=True, max_length=20, default="None")
	fD_odds = models.CharField(blank=True, max_length=20, default="None")
	number_14 = models.IntegerField(default=0)


	fD_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')

	## prediction multiple 1/5

	ffA_home_team = models.CharField(blank=True, max_length=100, default="None")
	ffA_away_team = models.CharField(blank=True, max_length=100, default="None")
	ffA_league = models.CharField(max_length=1000, blank=True , default="None")
	ffA_tip = models. CharField(blank=True, max_length=20, default="None")
	ffA_odds = models.CharField(blank=True, max_length=20, default="None")
	ffA_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_15 = models.IntegerField(default=0)

	ffB_home_team = models.CharField(blank=True, max_length=100, default="None")
	ffB_away_team = models.CharField(blank=True, max_length=100, default="None")
	ffB_league = models.CharField(max_length=1000, blank=True , default="None")
	ffB_tip = models. CharField(blank=True, max_length=20, default="None")
	ffB_odds = models.CharField(blank=True, max_length=20, default="None")
	ffB_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_16 = models.IntegerField(default=0)

	ffC_home_team = models.CharField(blank=True, max_length=100, default="None")
	ffC_away_team = models.CharField(blank=True, max_length=100, default="None")
	ffC_league = models.CharField(max_length=1000, blank=True , default="None")
	ffC_tip = models. CharField(blank=True, max_length=20, default="None")
	ffC_odds = models.CharField(blank=True, max_length=20, default="None")
	ffC_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_17 = models.IntegerField(default=0)

	ffD_home_team = models.CharField(blank=True, max_length=100, default="None")
	ffD_away_team = models.CharField(blank=True, max_length=100, default="None")
	ffD_league = models.CharField(max_length=1000, blank=True , default="None")
	ffD_tip = models. CharField(blank=True, max_length=20, default="None")
	ffD_odds = models.CharField(blank=True, max_length=20, default="None")
	ffD_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_18 = models.IntegerField(default=0)

	ffE_home_team = models.CharField(blank=True, max_length=100, default="None")
	ffE_away_team = models.CharField(blank=True, max_length=100, default="None")
	ffE_league = models.CharField(max_length=1000, blank=True , default="None")
	ffE_tip = models. CharField(blank=True, max_length=20, default="None")
	ffE_odds = models.CharField(blank=True, max_length=20, default="None")
	ffE_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_19 = models.IntegerField(default=0)

	## prediction multiple 1/6

	siA_home_team = models.CharField(blank=True, max_length=100, default="None")
	siA_away_team = models.CharField(blank=True, max_length=100, default="None")
	siA_league = models.CharField(max_length=1000, blank=True , default="None")
	siA_tip = models. CharField(blank=True, max_length=20, default="None")
	siA_odds = models.CharField(blank=True, max_length=20, default="None")
	siA_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_20 = models.IntegerField(default=0)

	siB_home_team = models.CharField(blank=True, max_length=100, default="None")
	siB_away_team = models.CharField(blank=True, max_length=100, default="None")
	siB_league = models.CharField(max_length=1000, blank=True , default="None")
	siB_tip = models. CharField(blank=True, max_length=20, default="None")
	siB_odds = models.CharField(blank=True, max_length=20, default="None")
	siB_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_21 = models.IntegerField(default=0)

	siC_home_team = models.CharField(blank=True, max_length=100, default="None")
	siC_away_team = models.CharField(blank=True, max_length=100, default="None")
	siC_league = models.CharField(max_length=1000, blank=True , default="None")
	siC_tip = models. CharField(blank=True, max_length=20, default="None")
	siC_odds = models.CharField(blank=True, max_length=20, default="None")
	siC_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_22 = models.IntegerField(default=0)

	siD_home_team = models.CharField(blank=True, max_length=100, default="None")
	siD_away_team = models.CharField(blank=True, max_length=100, default="None")
	siD_league = models.CharField(max_length=1000, blank=True , default="None")
	siD_tip = models. CharField(blank=True, max_length=20, default="None")
	siD_odds = models.CharField(blank=True, max_length=20, default="None")
	siD_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_23 = models.IntegerField(default=0)

	siE_home_team = models.CharField(blank=True, max_length=100, default="None")
	siE_away_team = models.CharField(blank=True, max_length=100, default="None")
	siE_league = models.CharField(max_length=1000, blank=True , default="None")
	siE_tip = models. CharField(blank=True, max_length=20, default="None")
	siE_odds = models.CharField(blank=True, max_length=20, default="None")
	siE_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_24 = models.IntegerField(default=0)

	siF_home_team = models.CharField(blank=True, max_length=100, default="None")
	siF_away_team = models.CharField(blank=True, max_length=100, default="None")
	siF_league = models.CharField(max_length=1000, blank=True , default="None")
	siF_tip = models. CharField(blank=True, max_length=20, default="None")
	siF_odds = models.CharField(blank=True, max_length=20, default="None")
	siF_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_25 = models.IntegerField(default=0)

	## prediction multiple 1/7

	sA_home_team = models.CharField(blank=True, max_length=100, default="None")
	sA_away_team = models.CharField(blank=True, max_length=100, default="None")
	sA_league = models.CharField(max_length=1000, blank=True , default="None")
	sA_tip = models. CharField(blank=True, max_length=20, default="None")
	sA_odds = models.CharField(blank=True, max_length=20, default="None")
	sA_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_26 = models.IntegerField(default=0)

	sB_home_team = models.CharField(blank=True, max_length=100, default="None")
	sB_away_team = models.CharField(blank=True, max_length=100, default="None")
	sB_league = models.CharField(max_length=1000, blank=True , default="None")
	sB_tip = models. CharField(blank=True, max_length=20, default="None")
	sB_odds = models.CharField(blank=True, max_length=20, default="None")
	sB_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_27 = models.IntegerField(default=0)

	sC_home_team = models.CharField(blank=True, max_length=100, default="None")
	sC_away_team = models.CharField(blank=True, max_length=100, default="None")
	sC_league = models.CharField(max_length=1000, blank=True , default="None")
	sC_tip = models. CharField(blank=True, max_length=20, default="None")
	sC_odds = models.CharField(blank=True, max_length=20, default="None")
	sC_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_28 = models.IntegerField(default=0)

	sD_home_team = models.CharField(blank=True, max_length=100, default="None")
	sD_away_team = models.CharField(blank=True, max_length=100, default="None")
	sD_league = models.CharField(max_length=1000, blank=True , default="None")
	sD_tip = models. CharField(blank=True, max_length=20, default="None")
	sD_odds = models.CharField(blank=True, max_length=20, default="None")
	sD_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_29 = models.IntegerField(default=0)

	sE_home_team = models.CharField(blank=True, max_length=100, default="None")
	sE_away_team = models.CharField(blank=True, max_length=100, default="None")
	sE_league = models.CharField(max_length=1000, blank=True , default="None")
	sE_tip = models. CharField(blank=True, max_length=20, default="None")
	sE_odds = models.CharField(blank=True, max_length=20, default="None")
	sE_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_30 = models.IntegerField(default=0)

	sF_home_team = models.CharField(blank=True, max_length=100, default="None")
	sF_away_team = models.CharField(blank=True, max_length=100, default="None")
	sF_league = models.CharField(max_length=1000, blank=True , default="None")
	sF_tip = models. CharField(blank=True, max_length=20, default="None")
	sF_odds = models.CharField(blank=True, max_length=20, default="None")
	sF_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_31 = models.IntegerField(default=0)

	gF_home_team = models.CharField(blank=True, max_length=100, default="None")
	gF_away_team = models.CharField(blank=True, max_length=100, default="None")
	gF_league = models.CharField(max_length=1000, blank=True , default="None")
	gF_tip = models. CharField(blank=True, max_length=20, default="None")
	gF_odds = models.CharField(blank=True, max_length=20, default="None")
	gf_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_32 = models.IntegerField(default=0)


	## both teams to score (gg)

	ggA_home_team = models.CharField(blank=True, max_length=100, default="None")
	ggA_away_team = models.CharField(blank=True, max_length=100, default="None")
	ggA_league = models.CharField(max_length=1000, blank=True , default="None")
	ggA_tip = models. CharField(blank=True, max_length=20, default="None")
	ggA_odds = models.CharField(blank=True, max_length=20, default="None")
	ggA_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_33 = models.IntegerField(default=0)

	ggB_home_team = models.CharField(blank=True, max_length=100, default="None")
	ggB_away_team = models.CharField(blank=True, max_length=100, default="None")
	ggB_league = models.CharField(max_length=1000, blank=True , default="None")
	ggB_tip = models. CharField(blank=True, max_length=20, default="None")
	ggB_odds = models.CharField(blank=True, max_length=20, default="None")
	ggB_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_34 = models.IntegerField(default=0)

	ggC_home_team = models.CharField(blank=True, max_length=100, default="None")
	ggC_away_team = models.CharField(blank=True, max_length=100, default="None")
	ggC_league = models.CharField(max_length=1000, blank=True , default="None")
	ggC_tip = models. CharField(blank=True, max_length=20, default="None")
	ggC_odds = models.CharField(blank=True, max_length=20, default="None")
	ggC_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_35 = models.IntegerField(default=0)

	ggD_home_team = models.CharField(blank=True, max_length=100, default="None")
	ggD_away_team = models.CharField(blank=True, max_length=100, default="None")
	ggD_league = models.CharField(max_length=1000, blank=True , default="None")
	ggD_tip = models. CharField(blank=True, max_length=20, default="None")
	ggD_odds = models.CharField(blank=True, max_length=20, default="None")
	ggD_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_36 = models.IntegerField(default=0)

	ggE_home_team = models.CharField(blank=True, max_length=100, default="None")
	ggE_away_team = models.CharField(blank=True, max_length=100, default="None")
	ggE_league = models.CharField(max_length=1000, blank=True , default="None")
	ggE_tip = models. CharField(blank=True, max_length=20, default="None")
	ggE_odds = models.CharField(blank=True, max_length=20, default="None")
	ggE_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_37 = models.IntegerField(default=0)


	ggF_home_team = models.CharField(blank=True, max_length=100, default="None")
	ggF_away_team = models.CharField(blank=True, max_length=100, default="None")
	ggF_league = models.CharField(max_length=1000, blank=True , default="None")
	ggF_tip = models. CharField(blank=True, max_length=20, default="None")
	ggF_odds = models.CharField(blank=True, max_length=20, default="None")
	ggF_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_38 = models.IntegerField(default=0)

	ggG_home_team = models.CharField(blank=True, max_length=100, default="None")
	ggG_away_team = models.CharField(blank=True, max_length=100, default="None")
	ggG_league = models.CharField(max_length=1000, blank=True , default="None")
	ggG_tip = models. CharField(blank=True, max_length=20, default="None")
	ggG_odds = models.CharField(blank=True, max_length=20, default="None")
	ggG_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_39 = models.IntegerField(default=0)

	ggH_home_team = models.CharField(blank=True, max_length=100, default="None")
	ggH_away_team = models.CharField(blank=True, max_length=100, default="None")
	ggH_league = models.CharField(max_length=1000, blank=True , default="None")
	ggH_tip = models. CharField(blank=True, max_length=20, default="None")
	ggH_odds = models.CharField(blank=True, max_length=20, default="None")
	ggH_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_40 = models.IntegerField(default=0)

	ggI_home_team = models.CharField(blank=True, max_length=100, default="None")
	ggI_away_team = models.CharField(blank=True, max_length=100, default="None")
	ggI_league = models.CharField(max_length=1000, blank=True , default="None")
	ggI_tip = models. CharField(blank=True, max_length=20, default="None")
	ggI_odds = models.CharField(blank=True, max_length=20, default="None")
	ggI_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_41 = models.IntegerField(default=0)

	ggJ_home_team = models.CharField(blank=True, max_length=100, default="None")
	ggJ_away_team = models.CharField(blank=True, max_length=100, default="None")
	ggJ_league = models.CharField(max_length=1000, blank=True , default="None")
	ggJ_tip = models. CharField(blank=True, max_length=20, default="None")
	ggJ_odds = models.CharField(blank=True, max_length=20, default="None")
	number_42 = models.IntegerField(default=0)

	ggJ_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')


	## correct Score (cc)

	ccA_home_team = models.CharField(blank=True, max_length=100, default="None")
	ccA_away_team = models.CharField(blank=True, max_length=100, default="None")
	ccA_league = models.CharField(max_length=1000, blank=True , default="None")
	ccA_tip = models. CharField(blank=True, max_length=20, default="None")
	ccA_odds = models.CharField(blank=True, max_length=20, default="None")
	ccA_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_43 = models.IntegerField(default=0)

	ccB_home_team = models.CharField(blank=True, max_length=100, default="None")
	ccB_away_team = models.CharField(blank=True, max_length=100, default="None")
	ccB_league = models.CharField(max_length=1000, blank=True , default="None")
	ccB_tip = models. CharField(blank=True, max_length=20, default="None")
	ccB_odds = models.CharField(blank=True, max_length=20, default="None")
	ccB_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_44 = models.IntegerField(default=0)

	ccC_home_team = models.CharField(blank=True, max_length=100, default="None")
	ccC_away_team = models.CharField(blank=True, max_length=100, default="None")
	ccC_league = models.CharField(max_length=1000, blank=True , default="None")
	ccC_tip = models. CharField(blank=True, max_length=20, default="None")
	ccC_odds = models.CharField(blank=True, max_length=20, default="None")
	ccC_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_45 = models.IntegerField(default=0)

	ccD_home_team = models.CharField(blank=True, max_length=100, default="None")
	ccD_away_team = models.CharField(blank=True, max_length=100, default="None")
	ccD_league = models.CharField(max_length=1000, blank=True , default="None")
	ccD_tip = models. CharField(blank=True, max_length=20, default="None")
	ccD_odds = models.CharField(blank=True, max_length=20, default="None")
	ccD_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_46 = models.IntegerField(default=0)

	ccE_home_team = models.CharField(blank=True, max_length=100, default="None")
	ccE_away_team = models.CharField(blank=True, max_length=100, default="None")
	ccE_league = models.CharField(max_length=1000, blank=True , default="None")
	ccE_tip = models. CharField(blank=True, max_length=20, default="None")
	ccE_odds = models.CharField(blank=True, max_length=20, default="None")
	ccE_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_47 = models.IntegerField(default=0)

	ccF_home_team = models.CharField(blank=True, max_length=100, default="None")
	ccF_away_team = models.CharField(blank=True, max_length=100, default="None")
	ccF_league = models.CharField(max_length=1000, blank=True , default="None")
	ccF_tip = models. CharField(blank=True, max_length=20, default="None")
	ccF_odds = models.CharField(blank=True, max_length=20, default="None")
	ccF_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_48 = models.IntegerField(default=0)

	ccG_home_team = models.CharField(blank=True, max_length=100, default="None")
	ccG_away_team = models.CharField(blank=True, max_length=100, default="None")
	ccG_league = models.CharField(max_length=1000, blank=True , default="None")
	ccG_tip = models. CharField(blank=True, max_length=20, default="None")
	ccG_odds = models.CharField(blank=True, max_length=20, default="None")
	ccG_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_49 = models.IntegerField(default=0)

	ccH_home_team = models.CharField(blank=True, max_length=100, default="None")
	ccH_away_team = models.CharField(blank=True, max_length=100, default="None")
	ccH_league = models.CharField(max_length=1000, blank=True , default="None")
	ccH_tip = models. CharField(blank=True, max_length=20, default="None")
	ccH_odds = models.CharField(blank=True, max_length=20, default="None")
	ccH_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_50 = models.IntegerField(default=0)

	ccI_home_team = models.CharField(blank=True, max_length=100, default="None")
	ccI_away_team = models.CharField(blank=True, max_length=100, default="None")
	ccI_league = models.CharField(max_length=1000, blank=True , default="None")
	ccI_tip = models. CharField(blank=True, max_length=20, default="None")
	ccI_odds = models.CharField(blank=True, max_length=20, default="None")
	ccI_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_51 = models.IntegerField(default=0)

	ccJ_home_team = models.CharField(blank=True, max_length=100, default="None")
	ccJ_away_team = models.CharField(blank=True, max_length=100, default="None")
	ccJ_league = models.CharField(max_length=1000, blank=True , default="None")
	ccJ_tip = models. CharField(blank=True, max_length=20, default="None")
	ccJ_odds = models.CharField(blank=True, max_length=20, default="None")
	number_52 = models.IntegerField(default=0)

	ccJ_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	create_at = models.DateTimeField(auto_now_add=True, null=True)

	## half Time Score(ht)

	htA_home_team = models.CharField(blank=True, max_length=100, default="None")
	htA_away_team = models.CharField(blank=True, max_length=100, default="None")
	htA_league = models.CharField(max_length=1000, blank=True , default="None")
	htA_tip = models. CharField(blank=True, max_length=20, default="None")
	htA_odds = models.CharField(blank=True, max_length=20, default="None")
	htA_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_53 = models.IntegerField(default=0)

	htB_home_team = models.CharField(blank=True, max_length=100, default="None")
	htB_away_team = models.CharField(blank=True, max_length=100, default="None")
	htB_league = models.CharField(max_length=1000, blank=True , default="None")
	htB_tip = models. CharField(blank=True, max_length=20, default="None")
	htB_odds = models.CharField(blank=True, max_length=20, default="None")
	htB_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_54 = models.IntegerField(default=0)

	htC_home_team = models.CharField(blank=True, max_length=100, default="None")
	htC_away_team = models.CharField(blank=True, max_length=100, default="None")
	htC_league = models.CharField(max_length=1000, blank=True , default="None")
	htC_tip = models. CharField(blank=True, max_length=20, default="None")
	htC_odds = models.CharField(blank=True, max_length=20, default="None")
	htC_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_55 = models.IntegerField(default=0)

	htD_home_team = models.CharField(blank=True, max_length=100, default="None")
	htD_away_team = models.CharField(blank=True, max_length=100, default="None")
	htD_league = models.CharField(max_length=1000, blank=True , default="None")
	htD_tip = models. CharField(blank=True, max_length=20, default="None")
	htD_odds = models.CharField(blank=True, max_length=20, default="None")
	htD_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_56 = models.IntegerField(default=0)

	htE_home_team = models.CharField(blank=True, max_length=100, default="None")
	htE_away_team = models.CharField(blank=True, max_length=100, default="None")
	htE_league = models.CharField(max_length=1000, blank=True , default="None")
	htE_tip = models. CharField(blank=True, max_length=20, default="None")
	htE_odds = models.CharField(blank=True, max_length=20, default="None")
	htE_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_57 = models.IntegerField(default=0)

	htF_home_team = models.CharField(blank=True, max_length=100, default="None")
	htF_away_team = models.CharField(blank=True, max_length=100, default="None")
	htF_league = models.CharField(max_length=1000, blank=True , default="None")
	htF_tip = models. CharField(blank=True, max_length=20, default="None")
	htF_odds = models.CharField(blank=True, max_length=20, default="None")
	htF_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_58 = models.IntegerField(default=0)

	htG_home_team = models.CharField(blank=True, max_length=100, default="None")
	htG_away_team = models.CharField(blank=True, max_length=100, default="None")
	htG_league = models.CharField(max_length=1000, blank=True , default="None")
	htG_tip = models. CharField(blank=True, max_length=20, default="None")
	htG_odds = models.CharField(blank=True, max_length=20, default="None")
	htG_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_59 = models.IntegerField(default=0)

	htH_home_team = models.CharField(blank=True, max_length=100, default="None")
	htH_away_team = models.CharField(blank=True, max_length=100, default="None")
	htH_league = models.CharField(max_length=1000, blank=True , default="None")
	htH_tip = models. CharField(blank=True, max_length=20, default="None")
	htH_odds = models.CharField(blank=True, max_length=20, default="None")
	htH_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_60 = models.IntegerField(default=0)

	htI_home_team = models.CharField(blank=True, max_length=100, default="None")
	htI_away_team = models.CharField(blank=True, max_length=100, default="None")
	htI_league = models.CharField(max_length=1000, blank=True , default="None")
	htI_tip = models. CharField(blank=True, max_length=20, default="None")
	htI_odds = models.CharField(blank=True, max_length=20, default="None")
	htI_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_61 = models.IntegerField(default=0)

	htJ_home_team = models.CharField(blank=True, max_length=100, default="None")
	htJ_away_team = models.CharField(blank=True, max_length=100, default="None")
	htJ_league = models.CharField(max_length=1000, blank=True , default="None")
	htJ_tip = models. CharField(blank=True, max_length=20, default="None")
	htJ_odds = models.CharField(blank=True, max_length=20, default="None")

	htJ_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_62 = models.IntegerField(default=0)

	## full Time score(hft)

	ftA_home_team = models.CharField(blank=True, max_length=100, default="None")
	ftA_away_team = models.CharField(blank=True, max_length=100, default="None")
	ftA_league = models.CharField(max_length=1000, blank=True , default="None")
	ftA_tip = models. CharField(blank=True, max_length=20, default="None")
	ftA_odds = models.CharField(blank=True, max_length=20, default="None")
	ftA_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_63 = models.IntegerField(default=0)

	ftB_home_team = models.CharField(blank=True, max_length=100, default="None")
	ftB_away_team = models.CharField(blank=True, max_length=100, default="None")
	ftB_league = models.CharField(max_length=1000, blank=True , default="None")
	ftB_tip = models. CharField(blank=True, max_length=20, default="None")
	ftB_odds = models.CharField(blank=True, max_length=20, default="None")
	ftB_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_64 = models.IntegerField(default=0)

	ftC_home_team = models.CharField(blank=True, max_length=100, default="None")
	ftC_away_team = models.CharField(blank=True, max_length=100, default="None")
	ftC_league = models.CharField(max_length=1000, blank=True , default="None")
	ftC_tip = models. CharField(blank=True, max_length=20, default="None")
	ftC_odds = models.CharField(blank=True, max_length=20, default="None")
	ftC_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_65 = models.IntegerField(default=0)

	ftD_home_team = models.CharField(blank=True, max_length=100, default="None")
	ftD_away_team = models.CharField(blank=True, max_length=100, default="None")
	ftD_league = models.CharField(max_length=1000, blank=True , default="None")
	ftD_tip = models. CharField(blank=True, max_length=20, default="None")
	ftD_odds = models.CharField(blank=True, max_length=20, default="None")
	ftD_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_66 = models.IntegerField(default=0)

	ftE_home_team = models.CharField(blank=True, max_length=100, default="None")
	ftE_away_team = models.CharField(blank=True, max_length=100, default="None")
	ftE_league = models.CharField(max_length=1000, blank=True , default="None")
	ftE_tip = models. CharField(blank=True, max_length=20, default="None")
	ftE_odds = models.CharField(blank=True, max_length=20, default="None")
	ftE_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_67 = models.IntegerField(default=0)

	ftF_home_team = models.CharField(blank=True, max_length=100, default="None")
	ftF_away_team = models.CharField(blank=True, max_length=100, default="None")
	ftF_league = models.CharField(max_length=1000, blank=True , default="None")
	ftF_tip = models. CharField(blank=True, max_length=20, default="None")
	ftF_odds = models.CharField(blank=True, max_length=20, default="None")
	ftF_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_68 = models.IntegerField(default=0)

	ftG_home_team = models.CharField(blank=True, max_length=100, default="None")
	ftG_away_team = models.CharField(blank=True, max_length=100, default="None")
	ftG_league = models.CharField(max_length=1000, blank=True , default="None")
	ftG_tip = models. CharField(blank=True, max_length=20, default="None")
	ftG_odds = models.CharField(blank=True, max_length=20, default="None")
	ftG_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_69 = models.IntegerField(default=0)

	ftH_home_team = models.CharField(blank=True, max_length=100, default="None")
	ftH_away_team = models.CharField(blank=True, max_length=100, default="None")
	ftH_league = models.CharField(max_length=1000, blank=True , default="None")
	ftH_tip = models. CharField(blank=True, max_length=20, default="None")
	ftH_odds = models.CharField(blank=True, max_length=20, default="None")
	ftH_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_70 = models.IntegerField(default=0)

	ftI_home_team = models.CharField(blank=True, max_length=100, default="None")
	ftI_away_team = models.CharField(blank=True, max_length=100, default="None")
	ftI_league = models.CharField(max_length=1000, blank=True , default="None")
	ftI_tip = models. CharField(blank=True, max_length=20, default="None")
	ftI_odds = models.CharField(blank=True, max_length=20, default="None")
	ftI_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_71 = models.IntegerField(default=0)

	ftJ_home_team = models.CharField(blank=True, max_length=100, default="None")
	ftJ_away_team = models.CharField(blank=True, max_length=100, default="None")
	ftJ_league = models.CharField(max_length=1000, blank=True , default="None")
	ftJ_tip = models. CharField(blank=True, max_length=20, default="None")
	ftJ_odds = models.CharField(blank=True, max_length=20, default="None")
	ftJ_result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
	number_72 = models.IntegerField(default=0)
	create_at = models.DateTimeField(auto_now_add=True, null=True)


class Contact(models.Model):
	STATUS = (
		('New', 'New'),
		('Read', 'Read'),
		('Closed', 'Closed'),
	)
	name = models.CharField(blank=True, max_length=20, null=True)
	email = models.CharField(blank=True, max_length=50, null=True)
	subject = models.CharField(blank=True, max_length=50, null=True)
	message = models.TextField(blank=True, max_length=1255, null=True)
	status = models.CharField(max_length=15, choices=STATUS, default='New')
	ip = models.CharField(blank=True, max_length=20, null=True)
	phone = models.CharField(blank=True, max_length=100, null=True)
	create_at = models.DateTimeField(auto_now_add=True, null=True)
	update_at = models.DateTimeField(auto_now=True, null=True)

	def __str__(self):
		return self.name

class ContactForm(ModelForm):
	class Meta:
		model = Contact
		fields = ['name', 'email', 'subject', 'message', 'phone']
		widgets = {
			'name'		: TextInput(attrs={'class': 'input','placeholder':'Name & Surname'}),
			'phone'		: TextInput(attrs={'class': 'input','placeholder':'Phone Number'}),
			'subject'	: TextInput(attrs={'class': 'input','placeholder':'Subject'}),
			'email'		: TextInput(attrs={'class': 'input','placeholder':'Email Address'}),
			'message'	: Textarea(attrs={'class': 'input', 'placeholder':'Your Message', 'rows':'5'}),

		}
