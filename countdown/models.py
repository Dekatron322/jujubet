from django.db import models
from django.utils import timezone
from django.forms import ModelForm, Textarea, TextInput, Select
# Create your models here.


class Subscribe(models.Model):
	email = models.CharField(blank=True, max_length=50, null=True)

class SubscribeForm(ModelForm):
	class Meta:
		model = Subscribe
		fields = ['email']
		widgets = {
			'email'		: TextInput(attrs={'class': 'input','placeholder':'Email Address'}),
		}


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
