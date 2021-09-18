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

	home_team = models.CharField(blank=True, max_length=100)
	away_team = models.CharField(blank=True, max_length=100)
	league = models.CharField(max_length=1000, blank=True )
	tip = models. CharField(blank=True, max_length=20)
	odds = models.CharField(blank=True, max_length=20)
	result = models.CharField(max_length=30, choices=RESULT, default='PENDING')
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
